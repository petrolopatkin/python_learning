import json
from expense import Expense
def save_expenses(expenses):
    blank = []
    for expense in expenses:
        saved_expenses = {
            "Date": expense.date,
            "Category": expense.category,
            "Item": expense.item,
            "Price": expense.price
        }
        blank.append(saved_expenses)
    with open("My projects/Expense Tracker v2/expenses.json", "w") as f:
        json.dump(blank, f, indent=2)


def load_expenses():
    with open("My projects/Expense Tracker v2/expenses.json", "r") as f:
        data = json.load(f)
    expenses = []
    for expense_data in data:
        expense = Expense(
            expense_data["Date"],
            expense_data["Category"],
            expense_data["Item"],
            expense_data["Price"]
        )
        expenses.append(expense)
    return expenses