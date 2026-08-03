#task1 classes practice
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    

    def show_info(self):
        print(f"{self.name} earns ${self.salary}")


    def give_raise(self, amount):
        print(f"{self.name} got a raise of ${amount}!")
        self.salary = self.salary + amount 


emp1 = Employee("Peter", 2000)
emp1.show_info()
emp1.give_raise(500)
emp1.show_info()
#task2 lists practice
numbers = [58, 8, 45, 12, 36, 97, 5, 26]
max_number = 0
min_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)
for number in numbers:
    if number < min_number:
        min_number = number
print(min_number)