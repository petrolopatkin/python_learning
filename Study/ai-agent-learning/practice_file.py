from datetime import date
from database import get_spending_by_month
from database import get_monthly_summary
from tools import get_monthly_spending_report

# spending = {
#     "description": "books",
#     "amount": 18.4,
#     "currency": "USD"
# }

# required_fields = ["description", "amount", "currency", "category"]

# for field in required_fields:
#     if field not in spending:
#         print(f"Missing field: {field}")

# spendings = get_spending_by_month(2026, 10)

# for spending in spendings:
#     print(spending)

# today = date.today()
# summary = get_monthly_summary(today.year, today.month)

# print(f"\nMonthly summary -- {today.strftime('%B %Y')}")
# print("-" * 35)

# if not summary["totals_by_currency"]:
#     print("No purchases found this month")
# else:
#     print("Total spending: ")

#     for currency, total in summary["totals_by_currency"].items():
#         print(f"  {currency}: {total:.2f}")

#     print("\nMost expensive purchases: ")

#     for currency, spending in summary["most_expensive_by_currency"].items():
#         description = spending["Description"]
#         amount = spending["Amount"]

#         print(f"  {currency}: {description} -- {amount:.2f} {currency}")

today = date.today()

report = get_monthly_spending_report(today.year, today.month)

print(report)