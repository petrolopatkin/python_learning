import os 
import json
import sys
from dotenv import load_dotenv
# from google import genai
from validators import validate_spending


def main():
    try:
        with open("Study/ai-agent-learning/response.json", "r", encoding="utf-8") as f:
            spending = json.load(f)
    except json.JSONDecodeError:
        print("Invalid JSON")
        return

    try:
        validate_spending(spending)
    except ValueError as err:
        print(f"Error: {err}")
        return

    print("\nExtracted spending:")
    print(json.dumps(spending, indent=4))

if __name__ == "__main__":
    main()

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     raise RuntimeError("GEMINI_API_KEY is not set")

# client = genai.Client(api_key=api_key)

# user_input = input("Describe your spending: ")

# response = client.models.generate_content(model="gemini-3.5-flash-lite", contents=f"""
# Extract information about the user's soending.
# Return a JSON object with these fields:
# - description: short description of the purchase
# - amount: numeric amount
# - currency: currency code, such as EUR or USD
# - category: spending category

# Do not invent information that is not present in the user's message.
# If as field in unknown use null.

# User message: {user_input}
# """, config={
#     "response_mime_type": "application/json",
#     "max_output_tokens": 200
# })

# spending = json.loads(response.text)
# print("Raw response:", response.text)
# print("Python type:", type(spending))


