import os 
import json
import pymysql
from dotenv import load_dotenv
from google import genai
from google.genai import errors
from google.genai import types
from datetime import date
from validators import validate_spending, validate_income
from database import save_spending, save_income, save_operations
from tools import get_monthly_spending_report, get_monthly_report_for_gemini, get_monthly_income_report_for_gemini
from logging_config import logger


def ask_gemini(client, user_input, today):
    response = client.models.generate_content(model="gemini-3.5-flash-lite", contents=f"""
    You are a financial transaction extraction assistant.

Your task is to identify all income and spending transactions explicitly mentioned in the user's message.

Today's date is {today}.

1. Transaction identification

Identify every separate financial transaction in the user's message.

Each transaction must have exactly one type:

- "income" — money received by the user.
- "spending" — money paid or spent by the user.

A single message may contain multiple transactions, including both income and spending.

Do not combine separate transactions into one operation.

2. Income structure

For every income transaction, extract:

- description: short description of the income source.
- amount: numeric amount.
- currency: currency code, such as EUR or USD.
- income_date: date in YYYY-MM-DD format.

3. Spending structure

For every spending transaction, extract:

- description: short description of the purchase.
- amount: numeric amount.
- currency: currency code, such as EUR or USD.
- category: appropriate spending category.
- purchase_date: date in YYYY-MM-DD format, or null if unknown.

4. Date handling

Use today's date to interpret relative dates:

- "today" means today's date.
- "yesterday" means one day before today's date.
- If the user provides a specific date, use that date.
- If the date is not provided or cannot be determined, use null.

5. Data accuracy

- Do not invent information that is not present in the user's message.
- Do not confuse income with spending.
- Do not treat transfers between the user's own accounts as income or spending.
- Do not treat refunds as ordinary income; classify them according to their context.
- If a required field is unknown, do not guess its value. Use null.
- Amount must be numeric and must preserve the value stated by the user.
- Currency must be a currency code when it can be identified.
- Never use generic placeholder descriptions such as "Spent money", "Purchase", "Other expense"
- If the user does not specify what they bought or what the money was spent on, set description to null
- Never invent a description just to fill a required field 
- If description is null, preserve it as null in the JSON output

6. Output format

Return this JSON structure:

{{
    "operations": [
        {{
            "type": "income",
            "data": {{
                "description": "Part-time job"
            }}
        }}
    ]
}}

The operations array may contain one or multiple transactions.

If no income or spending transactions are found, return an empty operations array.

Return valid JSON only. Do not include Markdown, explanations, or text outside the JSON object.

User message: {user_input}
    """, config={
    "response_mime_type": "application/json",
    "max_output_tokens": 200
    })

    return response.text


def ask_report_agent(client, user_input):
    response = client.models.generate_content(model="gemini-3.5-flash-lite", contents=user_input,
               config=types.GenerateContentConfig(
                   tools=[get_monthly_report_for_gemini,
                          get_monthly_income_report_for_gemini],
                   system_instruction=(
                       "You are a personal finance assistant."
                        "Use the monthly spending report tool when the user asks about recorded expenses."
                        "Use the monthly income report tool when the user asks about recorded income."
                        "Never confuse income with spending."
                        "The current date is provided by the application."
                        "Never guess the year or month."
                        "If the requested period is the current month, use the current year and month from the application."
                        "Base your answers on the tool results and never invent financial data."
                   ),
               ),
            )

    return response.text


def parse_operations(raw_response):
    response = json.loads(raw_response)

    if not isinstance(response, dict):
        raise ValueError("Expected a JSON object")

    if "operations" not in response:
        raise ValueError("Missing required field: operations")

    operations = response["operations"]

    if not isinstance(operations, list):
        raise ValueError("Operations must be a list")

    validated_operations = []

    pending_operation = None

    for operation in operations:
        if not isinstance(operation, dict):
            raise ValueError("Each operation must be a JSON object")

        if "type" not in operation or "data" not in operation:
            raise ValueError("Each operation must contain type and data")

        operation_type = operation["type"]
        data = operation["data"]

        if not isinstance(data, dict):
            raise ValueError("Operation data must be a JSON object")

        if operation_type == "spending":
            if data["description"] is None:
                pending_operation = operation
            else:
                validate_spending(data)
                validated_operations.append(operation)
        elif operation_type == "income":
            if data["description"] is None:
                pending_operation = operation
            else:
                validate_income(data)
                validated_operations.append(operation)
        else:
            raise ValueError(f"Unknown operation type {operation_type}")

    return validated_operations, pending_operation


def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")

    client = genai.Client(api_key=api_key)

    pending_operation = None

    while True:
        user_input = input("Describe your spending: ")

        if user_input.strip().lower() == "exit":
            print("Goodbye!")
            break

        elif user_input.strip().lower().startswith("ask"):
            question = user_input.strip()[4:]

            logger.info("Report agent request received")

            try:
                answer = ask_report_agent(client, question)
                logger.info("Report agent response generated successfully")
                print(f"\n{answer}")

            except errors.APIError as err:
                logger.exception("Gemini API request failed")
                print(f"Error: Gemini API request failed {err}")

            except (ValueError, TypeError) as err:
                logger.exception("Report agent failed")
                print(f"Error: Agent failed {err}")

            continue

        elif user_input.strip().lower() == "report":
            today = date.today()

            report = get_monthly_spending_report(today.year, today.month)

            print(f"\nMonthly spending report -- {today.strftime('%B, %Y')}")

            if not report["totals_by_currency"]:
                print("No purchases found this month")

            else:
                print("\nTotal spending:")

                for currency, total in report["totals_by_currency"].items():
                    print(f"  {currency}: {total:.2f}")

                print("\nMost expensive purchases:")

                for currency, purchase in report["most_expensive_by_currency"].items():
                    description = purchase["Description"]
                    amount = purchase["Amount"]
                    category = purchase["category"]
                    purchase_date = purchase["purchase_date"]

                    print(f"  {currency}: {description} -- {amount:.2f} {currency}")
                    print(f"  Category: {category}")
                    print(f"  Date: {purchase_date}")
            continue

        if pending_operation is not None:
            pending_operation["data"]["description"] = user_input

            if pending_operation["type"] == "spending":
                validate_spending(pending_operation["data"])
            elif pending_operation["type"] == "income":
                validate_income(pending_operation["data"])

            save_operations([pending_operation])
            pending_operation = None
            print("Operation saved successfully")
            continue

        try:
            today = date.today()
            raw_response = ask_gemini(client, user_input, today)

        except errors.APIError as err:
            logger.exception("Gemini API request failed")
            print(f"Error: Gemini API request failed: {err}")
            continue

        try:
            operations, pending_operation = parse_operations(raw_response)

        except json.JSONDecodeError:
            print("Error: Gemini returned invalid JSON")
            continue

        except ValueError as err:
            print(f"Error: {err}")
            continue

        try:
            if operations:
                save_operations(operations)

        except pymysql.MySQLError as err:
            print(f"Error: Failed to save operations: {err}")
            continue

        except ValueError as err:
            print(f"Error: {err}")
            continue

        if pending_operation is not None:
            if pending_operation["type"] == "spending":
                print("What did you spend the money on?")
            else:
                print("What was the source of this income?")

        elif operations:
            print("Operations saved to database")
            print("\nExtracted operations:")
            print(json.dumps(operations, indent=4))

        else:
            print("No financial transactions found.")

if __name__ == "__main__":
    main()