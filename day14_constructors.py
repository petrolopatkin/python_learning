class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("move")


    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.y)
#task1
class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f"{self.name} is talking")


    def sing(self):
        print(f"{self.name} is singing")


person = Person("Peter")
person.talk()

mary = Person("Mary")
mary.sing()