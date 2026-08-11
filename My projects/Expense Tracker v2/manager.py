from expense import Expense
class ExpenseManager:
    def __init__(self):
       self.expenses = []


    def add_expense(self, expense):
        self.expenses.append(expense)


    def show_expenses(self):
        for expense in self.expenses:
            expense.show()


    def count_expenses(self):
        number = 0
        for expense in self.expenses:
            number += 1
        return number


    def total_price(self):
        total = 0
        for expense in self.expenses:
            total += expense.price
        return total 


    