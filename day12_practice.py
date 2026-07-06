#task1
def greeting(name):
    print(f"Hello, {name}!")
    print("Welcome back")


print("Start")
greeting("Peter")
greeting("Michael")
greeting("Kate")
print("Finish")
#task2
def multiply(a, b):
    return a * b


a = int(input("Enter a first number "))
b = int(input("Enter a second number "))
print(multiply(a, b))
#task3
try:
    number = int(input("Enter a number "))
    print(number)
except ValueError:
    print("Invalid value")
#task4+5
def division(c, d):
        return c/d
try:
    c = int(input("Enter a first number "))
    d = int(input("Enter a second number "))
    
    print(division(c, d))
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("You cant divise by 0")
#task6
def add(k, l):
        return k + l


def subtract(p, q):
        return p - q


def multiply(r, t):
        return r * t


def divide(g, h):
        return g/h


print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
choise = int(input("Choise an option "))
if choise == 1:
    try:
        k = int(input("Enter a number "))
        l = int(input("Enter a number "))
        print(add(k, l))
    except ValueError:
         print("Invalid value")
elif choise == 2:
    try:
        p = int(input("Enter a number "))
        q = int(input("Enter a number "))
        print(subtract(p, q))
    except ValueError:
         print("Invalid value")

elif choise == 3:
    try:
        r = int(input("Enter a number "))
        t = int(input("Enter a number "))
        print(multiply(r, t))
    except ValueError:
         print("Invalid value")
elif choise == 4:
    try:
        g = int(input("Enter a number "))
        h = int(input("Enter a number "))
        print(divide(g, h))
    except ValueError:
         print("Invalid value")
    except ZeroDivisionError:
         print("You cannot divide by 0")
else:
    print("Invalid option")

