import os


def clear():
   os.system("cls")


def show_expenses():
    with open("My projects/Expense Tracker/tracker.txt", "r") as file:
        for line in file:
            line = line.strip()
            date, category, item, price = line.split("|")
            print(f"""================================
Date: {date}
Category: {category}
Item: {item}
Price: {price}""")


def add_expense():
    date = int(input("Enter a date(DD-MM-YYYY): "))
    category = input("Category: ")
    item = input("Item: ")
    price = int(input("Price: "))
    with open("My projects/Expense Tracker/tracker.txt", "a") as file:
        file.write(f"{date}|{category}|{item}|{price}\n")
    print("Expense was successfully added")


def total_spent():
    pass


def delete_expense():
    pass


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