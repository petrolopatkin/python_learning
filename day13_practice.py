#task1
class Person:
    def introduce(self):
        print("introduce")


    def walk(self):
        print("walk")


point1 = Person()
point1.x = "Hello! I am Peter"
print(point1.x)
point2 = Person()
point2.x = "Peter is walking"
print(point2.x)
#task2
class Car:
    def start_engine(self):
        print("Engine is started")


    def stop_engine(self):
        print("Engine is stopped")


    def drive(self):
        print("Car is driving")


car = Car()
car.start_engine()
car.stop_engine()
car.drive()
#task3
class Calculator:
    def add(self, a, b):
        print(a + b)


    def subtract(self, a, b):
        print(a - b)


    def multiply(self, a, b):
        print(a * b)


calc = Calculator()
calc.add(6, 7)
calc.subtract(6, 7)
calc.multiply(6, 7)
#task4
class BankAccount:
    def deposit(self, amount):
        print(f"Deposited, {amount} ")
    

    def withdraw(self, amount):
        print(f"Withdrawn, {amount} ")

    
    def show_balance(self):
        print("Current balance")


acc = BankAccount()
acc.deposit(500)
acc.withdraw(200)
#task5
class Cube:
    def volume(self, side):
        return side * side * side
    

cube = Cube()
print(cube.volume(4))
#task6
class Dog:
    def bark(self):
        print(f"{self.name} is barking ")


    def eat(self):
        print(f"{self.name} is eating ")

    
    def sleep(self):
        print(f"{self.name} is sleeping")


dog1 = Dog()
dog1.name = "Baloon"
dog2 = Dog()
dog2.name = "Oscar"
dog3 = Dog()
dog3.name = "T-Rex"
dog1.bark()
dog2.eat()
dog3.sleep()
#task7
class Student:
    def study(self):
        print(f"{self.name} is studying")

    
    def play_games(self):
        print(f"{self.name} is playing viedo games")


    def relax(self):
        print(f"{self.name} is relaxing")


std1 = Student()
std1.name = "Peter"
std2 = Student()
std2.name = "Jhon"
std3 = Student()
std3.name = "Kate"
std1.study()
std2.play_games()
std3.relax()