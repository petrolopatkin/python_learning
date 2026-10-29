import os 
import json
import pymysql
from dotenv import load_dotenv
from google import genai
from google.genai import errors
from google.genai import types
from datetime import date
from validators import validate_spending
from database import save_spending
from tools import get_monthly_spending_report
from tools import get_monthly_report_for_gemini


def ask_gemini(client, user_input, today):
    response = client.models.generate_content(model="gemini-3.5-flash-lite", contents=f"""
    Extract information about the user's spending.

    Today's date is {today}.
    Use this date to interpret relative dates:
    - "today" means today's date.
    - "yesterday" means one day before today's date.
    - If the user gives a specific date, use that date.
    - If the purchase date is not provided or cannot be determined,
    set purchase_date to null.

    Return exactly one JSON object, not an array. 
    The response must start with "{{" and end with "}}" 
    Do not wrap the object in a list:
    - description: short description of the purchase
    - amount: numeric amount
    - currency: currency code, such as EUR or USD
    - category: spending category
    - purchase_date: date in YYYY-MM-DD format, or null

    Do not invent information that is not present in the user's message.
    If a field is unknown use null.
     
    User message: {user_input}
    """, config={
    "response_mime_type": "application/json",
    "max_output_tokens": 200
    })

    return response.text


def ask_report_agent(client, user_input):
    response = client.models.generate_content(model="gemini-3.5-flash-lite", contents=user_input,
               config=types.GenerateContentConfig(
                   tools=[get_monthly_report_for_gemini],
                   system_instruction=(
                       "You are a personal spending assistant."
                       "Use the monthly report tool when the user asks about recorded spending."
                       "The current date is provided by the application"
                       "Never guess the year or month"
                       "If the requested period is the current month use the current year and month from application"
                       "Base your answer on the tool result and never invent financial data"
                   ),
               ),
            )

    return response.text


def parse_spending(raw_response):
    spending = json.loads(raw_response)
    validate_spending(spending)

    return spending


def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")

    client = genai.Client(api_key=api_key)

    while True:     
        user_input = input("Describe your spending: ")

        if user_input.strip().lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.strip().lower().startswith("ask"):
            question = user_input.strip()[4:]

            try:
                answer = ask_report_agent(client, question)
                print(f"\n{answer}")
            except errors.APIError as err:
                print(f"Error: Gemini API request failed {err}")
            except (ValueError, TypeError) as err:
                print(f"Error: Agent failed {err}")
            continue

        elif user_input.strip().lower() == "report":
            today = date.today()

            report = get_monthly_spending_report(today.year, today.month)

            print(f"\nMonthly spending report -- {today.strftime('%B, %Y')}")
            
            if not report["totals_by_currency"]:
                print("No purchases found this month")
            else:
                print(f"\nTotal spending: ")

            for currency, total in report["totals_by_currency"].items():
                print(f"  {currency}: {total:.2f}")

                print("\n Most expensive purchases:")

                for currency, purchase in report["most_expensive_by_currency"].items():
                    description = purchase["Description"]
                    amount = purchase["Amount"]
                    category = purchase["category"]
                    purchase_date = purchase["purchase_date"]

                    print(f"  {currency}: {description} -- {amount:.2f} {currency}")
                    print(f"  Category: {category}")
                    print(f"  Date: {purchase_date}")

        else:
            try:
                today = date.today()
                raw_response = ask_gemini(client, user_input, today)
            except errors.APIError as err:
                print(f"Error: Gemini API request failed: {err}")
                continue

            try:
                spending = parse_spending(raw_response)
            except json.JSONDecodeError:
                print("Error: Gemini returned invalid JSON")
                continue
            except ValueError as err:
                print(f"Error: {err}")
                continue

            try:
                save_spending(spending)
            except pymysql.MySQLError as err:
                print(f"Error: Failed to save spending: {err}")
                continue

            print("Spending saved to database")

            print("\n Extracted spending:")
            print(json.dumps(spending, indent=4))

if __name__ == "__main__":
    main()