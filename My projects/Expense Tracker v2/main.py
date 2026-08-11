from expense import Expense
from manager import ExpenseManager
from storage import save_expenses
from storage import load_expenses
orange = Expense("09-08-2026", "Food", "Orange", 1.45)
tshirt = Expense("10-08-2026", "Shopping", "T-Shirt", 18.5)
manager = ExpenseManager()
manager.add_expense(orange)
manager.add_expense(tshirt)
manager.show_expenses()
print(manager.count_expenses())
print(manager.total_price())
save_expenses(manager.expenses)
expenses = load_expenses()
for expense in expenses:
    expense.show()