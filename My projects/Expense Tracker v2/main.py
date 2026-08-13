from expense import Expense
from manager import ExpenseManager
from storage import save_expenses
from storage import load_expenses
manager = ExpenseManager()
manager.expenses = load_expenses()
while True: 
    print("""
1. Add expense
2. Delete expense
3. Show expenses
4. Find by category
5. Total price
6. Exit
""")
    try: 
     choice = int(input("> "))
    except ValueError:
       print("Invalid value, try again")
       continue
    if choice == 1:
       manager.add_expense()
    elif choice == 2:
       manager.delete_expense()
    elif choice == 3:
       manager.show_expenses()
    elif choice == 4:
       category = input("Category: ")
       manager.find_category(category)
    elif choice == 5:
       print(manager.total_price())
    elif choice == 6:
       break
    else:
       print("Invalid value, try again")