#task1 practice with classes
class Phone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery


    def call(self, name):
        print(f"Calling {name}")

    
    def charge(self):
        print(f"{self.brand} {self.model} is charging, battery is {self.battery}")


    def show_info(self):
        print(f"{self.brand}, {self.model}, battery is {self.battery}")


xiaomi = Phone("Xiaomi", "Redmi Note 13", "90%")
xiaomi.call("Peter")
xiaomi.charge()
xiaomi.show_info()
samsung = Phone("Samsung", "S24 Ultra", "75%")
samsung.call("Kate")
samsung.show_info()
samsung.charge()
#task2 dictionaries practice
students = {
    "Jhon": 75,
    "Kate": 92,
    "Mosh": 87,
    "Peter": 99,
    "Max": 40,
    "Daniel": 67
}
grade = 0
best_student = " "
for item in students:
    best_grade = students[item]
    if best_grade > grade:
        grade = best_grade
        best_student = item
print(best_student, grade)
#task3 PiPy
import colorama
print("Library imported successfully!")
#task4 random game again pc
import random
secret_number = random.randint(1, 10)
count_times = 3
guess_count = 0
while guess_count < count_times:
    guess = int(input("Take a guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Congrats! You've won")
        break
    elif guess_count == count_times:
        print(f"Sorry, you've lost. The secret number was: {secret_number}")
        break
    else:
        print("Your guess is incorrect, try again!")