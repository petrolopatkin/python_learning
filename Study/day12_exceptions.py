try:
    age = int(input("Age: "))
    income = 50000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")