import os


def clear():
   os.system("cls")


def show_expenses():
    with open("My projects/Expense Tracker/tracker.txt", "r") as file:
        if not line:
            print("There are no expenses yet")
        for line in file:
            line = line.strip()
            date, category, item, price = line.split("|")
            print(f"""================================
Date: {date}
Category: {category}
Item: {item}
Price: {price}""")


def add_expense():
    date = input("Enter a date(DD-MM-YYYY): ")
    category = input("Category: ")
    item = input("Item: ")
    price = float(input("Price: "))
    with open("My projects/Expense Tracker/tracker.txt", "a") as file:
        file.write(f"{date}|{category}|{item}|{price}\n")
    print("Expense was successfully added")


def total_spent():
    total_price = 0
    with open("My projects/Expense Tracker/tracker.txt", "r") as file:
        spent = file.readlines()
        for line in spent:
            date, category, item, price = line.split("|")
            print(f"""================================
Date: {date}
Category: {category}
Item: {item}
Price: {price}""")
            price = float(price)
            total_price += price
        print(f"Total spent: {total_price}")


def delete_expense():
    with open("My projects/Expense Tracker/tracker.txt", "r") as file:
        expenses = file.readlines()
        if not expenses:
            print("There are no expences yet")
            return
        number = 1
        for expense in expenses:
            print(f"{number}. {expense}")
            number += 1
        del_expense = int(input("Which expense you want to delete? "))
        if del_expense < 1 or del_expense > len(expenses):
            print("Invalid expense")
            return
        while True:
            warning_message = input("Are you sure you want to delete this expense? ").lower()
            if warning_message == "y":
                expenses.pop(del_expense - 1)
                break
            elif warning_message == "n":
                print("You have cancelled a deletion")
                return
            else:
                print("You picked incorrect answer, try again")
                continue
        with open("My projects/Expense Tracker/tracker.txt", "w") as file:
            for expense in expenses:
                file.write(expense)
    show_expenses()
        
        


while True:
    print("""
1. Show expenses
2. Add expense
3. Show total spent
4. Delete expense
5. Exit""")
    try:
        command = int(input("> "))
    except ValueError:
        print("Wrong command, try again")
        continue
    if command == 1:
        show_expenses()
        input("Press ENTER to continue")
        clear()
    elif command == 2:
        add_expense()
        input("Press ENTER to continue")
        clear()
    elif command == 3:
        total_spent()
        input("Press ENTER to continue")
        clear()
    elif command == 4:
        delete_expense()
        input("Press ENTER to continue")
        clear()
    elif command == 5:
        break
    else:
        print("Wrong command, try again")