#task1
class Animal:
    def __init__(self, name):
        self.name = name


    def eat(self):
        print(f"{self.name} is eating")


    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


class Lion(Animal):
    def roar(self):
        print(f"{self.name} is roaring")


dog = Dog("T-Rex")
dog.sleep()
dog.bark()
lion = Lion("Simba")
lion.eat()
lion.roar()
#task2
class Vehicle:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


    def start_engine(self):
        print(f"{self.brand}'s engine is started")


    def stop_engine(self):
        print(f"{self.brand}'s engine is stopped")


class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} {self.color} color {self.year} is driving")


class Motorcycle(Vehicle):
    def ride(self):
        print(f"{self.brand} {self.color} color {self.year} is riding")


car = Car("Mazda MX-5 Miata", "red", 1989)
car.start_engine()
car.drive()
car.stop_engine()
motorcycle = Motorcycle("Yamaha V-Max", "black", 1985)
motorcycle.start_engine()
motorcycle.ride()
motorcycle.stop_engine()
#task3
class Character:
    def __init__(self, name):
        self.name = name
    

    def move(self):
        print(f"{self.name} is moving")


    def attack(self):
        print(f"{self.name} is attacking")


class Warrior(Character):
    def use_sword(self):
        print(f"{self.name} is attacking with a sword")

class Mage(Character):
    def cast_spell(self):
        print(f"{self.name} is casting a spell")

class Archer(Character):
    def shoot_arrow(self):
        print(f"{self.name} is shooting an arrow")


warriror = Warrior("Jerk")
warriror.move()
warriror.attack()
warriror.use_sword()
mage = Mage("Jack")
mage.move()
mage.attack()
mage.cast_spell()
archer = Archer("Kate")
archer.move()
archer.attack()
archer.shoot_arrow()