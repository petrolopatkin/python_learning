from datetime import date
from database import get_spending_by_month
from database import get_monthly_summary

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

summary = get_monthly_summary(2026, 10)

print(summary)