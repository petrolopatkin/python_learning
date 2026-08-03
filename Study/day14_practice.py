#task1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old")


bob = Person("Bob" , 19)
bob.introduce()
#task2
class Dog:
    def __init__(self, name):
        self.name = name


    def bark(self):
        print(f"{self.name} is barking")


    def eat(self):
        print(f"{self.name} is eating")


    def sleep(self):
        print(f"{self.name} is sleeping")


dog1 = Dog("Baloon")
dog1.bark()
dog2 = Dog("T-Rex")
dog2.eat()
dog3 = Dog("Oscar")
dog3.sleep()
#task3
class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


    def show_info(self):
        print(f"This is {self.brand} {self.color} color {self.year}")


    def start_engine(self):
        print("Engine is started")


    def drive(self):
        print("Car is driving")


    def stop_engine(self):
        print("Engine is stopped")

    
car = Car("Bentley", "Olive", 2024)
car.show_info()
car.start_engine()
car.drive()
car.stop_engine()
#task4
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


    def show_result(self):
        print(f"{self.name} {self.score}")
        if self.score >= 60:
            print("Passed")
        else:
            print("Failed")


std1 = Student("Peter", 100)
std1.show_result()
std2 = Student("Jhon", 58)
std2.show_result()
std3 = Student("Kate", 98)
std3.show_result()
#task5
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    
    def deposit(self, amount):
        print(f"{self.owner} deposited {amount}")


    def withdraw(self, amount):
        print(f"{self.owner} withdrawn {amount}")


    def show_balance(self):
        print(f"Current balance: {self.balance}")


acc = BankAccount("Peter", 1000)
acc.deposit(500)
acc.show_balance()
#task6
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height
    

    def perimeter(self):
        return 2 * (self.width + self.height)
    

rec = Rectangle(6, 7)
print(rec.area())
print(rec.perimeter())
#task7
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def open_book(self):
        print("Books is opened")


    def show_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Amount of pages: {self.pages}")


book1 = Book("Norwegian wood", "Haruki Murakami", 320)
book1.open_book()
book1.show_info()
book2 = Book("1984", "George Orwell", 400)
book2.open_book()
book2.show_info()
book3 = Book("Afternight", "Haruki Murakami", 208)
book3.open_book()
book3.show_info()