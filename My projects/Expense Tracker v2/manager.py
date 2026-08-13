from expense import Expense
from storage import save_expenses
class ExpenseManager:
    def __init__(self):
       self.expenses = []


    def add_expense(self):
        date = input("Date: ")
        category = input("Category: ")
        item = input("Item: ")
        price = float(input("Price: "))
        expense = Expense(date, category, item, price)
        self.expenses.append(expense)
        save_expenses(self.expenses)


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


    def find_category(self, category):
        for expense in self.expenses:
            if category == expense.category:
                expense.show()


    def delete_expense(self):
        number = 1
        for expense in self.expenses:
            print(f"{number}. ")
            expense.show()
            number += 1
        del_message = int(input("Which expense you want to delete? "))
        if del_message < 1 or del_message > len(self.expenses):
            print("Invalid expense")
            return
        while True:
            warning_message = input("Are you sure you want to delete this expense? ").lower()
            if warning_message == "y":
             self.expenses.pop(del_message - 1)
             print("Your deletion is successfull")
             save_expenses(self.expenses)
             break
            elif warning_message == "n":
                print("You have cancelled a deletion")
                return
            else:
             print("You picked incorrect answer, try again")
             continue