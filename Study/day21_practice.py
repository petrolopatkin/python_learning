#task1 classes practice
class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
    def show_info(self):
        print(f"This is a {self.brand} laptop with {self.ram} ram and {self.storage} storage")
    

    def turn_on(self):
        print(f"{self.brand} laptop is turned on")

    
    def turn_off(self):
        print(f"{self.brand} laptop is turned off")


samsung = Laptop("Samsung", "16 GB", "512 GB")
samsung.show_info()
samsung.turn_on()
samsung.turn_off()
lenovo = Laptop("Lenovo", "32 GB", "1 TB")
lenovo.show_info()
lenovo.turn_on()
lenovo.turn_off()


#task2 inheritance practice
class Employee:
    def work(self):
        print(f"{self.__class__.__name__} is working")


class Programmer(Employee):
    def write_code(self):
     print("A Programmer is writing a code")


class Designer(Employee):
    def draw_design(self):
        print("Designer is drawing design")


programmer = Programmer()
programmer.work()
programmer.write_code()
designer = Designer()
designer.work()
designer.draw_design()

#task 3 dictionaries practice
tech = {
    "PC": 2000,
    "Fridge": 1000,
    "TV": 2500,
    "Laptop" : 800,
    "Phone": 400,
    "NewTech": 3500
}
biggest_price = 0
most_expensive_item = " "
for item in tech:
    price = tech[item]
    if price > biggest_price:
        biggest_price = price
        most_expensive_item = item
print(most_expensive_item, biggest_price)