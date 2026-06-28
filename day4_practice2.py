#Task1
age_above_18 = True
has_a_ticket = True
if age_above_18 and has_a_ticket:
    print("Access allowed")
else:
    print("Access denied")
#Task2
age = int(input("Enter your age: "))
if age < 18 or age > 65:
    print("Discount available")
else:
    print("No discount")
#Task3
password = input("Enter password: ")
password == "hakunamatata"
blocked = False
if password == "hakunamatata" and not blocked:
    print("Accsess allowed")
else:
    print("Accsess denied")
#Task4
age=int(input("Enter your age: "))
has_a_subscription = True
if age >= 18 and has_a_subscription or age > 60:
    print("Accsess allowed")
else:
    print("Access denied")