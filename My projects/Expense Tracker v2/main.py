from expense import Expense
from manager import ExpenseManager

orange = Expense("09-08-2026", "Food", "Orange", 1.45)

manager = ExpenseManager()
manager.add_expense(orange)
manager.show_expenses()
print(manager.count_expenses())
print(manager.total_price())