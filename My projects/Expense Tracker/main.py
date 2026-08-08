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
        
        
def choose_category():
    categories = {
        1: "Food",
        2: "Entertainment",
        3: "Transport",
        4: "Sport",
        5: "Shopping",
        6: "Bills",
        7: "Other",
        8: "All"
    }
    print("""
1. Food
2. Entertainment
3. Transport
4. Sport
5. Shopping
6. Bills
7. Other
8. All Categories""")
    try:
     choice = int(input("Choose a category: "))
    except ValueError:
        print("Please enter a number")
        return None
    if choice in categories:
        return categories[choice]
    else:
        print("You have chosen wrong category, try again!")
        return None


def show_category():
    selected_category = choose_category()
    if selected_category is None:
        return 
    elif selected_category == "All":
        show_expenses()
        return
    with open("My projects/Expense Tracker/tracker.txt", "r") as file:
        cat = file.readlines()
        if not cat:
            print("There are no expenses yet")
            return
        found = False
        for line in cat:
         line = line.strip()
         date, category, item, price = line.split("|")
         if category == selected_category:
             found = True
             print(f"""================================
Date: {date}
Category: {category}
Item: {item}
Price: {price}""")
        if not found:
             print("There is no expense in this category yet")
            

while True:
    print("""
1. Show expenses
2. Add expense
3. Show total spent
4. Delete expense
5. Show category
6. Exit""")
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
        show_category()
        input("Press ENTER to continue")
        clear()
    elif command == 6:
        break
    else:
        print("Wrong command, try again")