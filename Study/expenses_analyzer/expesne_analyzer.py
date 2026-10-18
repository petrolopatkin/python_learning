expenses = [
    {"category": "Food", "amount": 12.50},
    {"category": "Transport", "amount": 2.80},
    {"category": "Food", "amount": 8.20},
    {"category": "Entertainment", "amount": 15.00},
    {"category": "Transport", "amount": 1.60},
    {"category": "Food", "amount": 6.40},
    {"category": "Education", "amount": 25.00},
]

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_by_category(expenses, category):
    category_total = 0
    for expense in expenses:
        if expense["category"] == category:
            category_total += expense["amount"]
    return category_total


def find_large_expenses(expenses, limit):
    large_expenses = []
    for expense in expenses:
        if expense["amount"] > limit:
            large_expenses.append(f"""
Category: {expense["category"]}
Amount: {expense["amount"]}""")
    return large_expenses


def calculate_all_categories(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += amount

    return category_totals


# print(calculate_total(expenses))
# print(calculate_by_category(expenses, "Food"))
# print(find_large_expenses(expenses, 10))
print(calculate_all_categories(expenses))