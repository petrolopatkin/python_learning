from dataclasses import dataclass 
from dataclasses import field
@dataclass
class Person:
    name: str
    age: int
    password: str = field(repr=False)
    is_alive: bool = True


    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")


person1 = Person("Spongebob", 30, "pineapple123")
person2 = Person("Patrick", 35, "star123456")

print(person1)
print(person2)
# (frozen=True) to froze our class(can't change anything within class object)
# (order=True) to compare objects
@dataclass
class Rectangle:
    width: float
    height: float 

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def describe(self) -> None:
        print(f"{self}")
        print(f"Area: {self.area}")
        print(f"Perimeter: {self.perimeter}")

rect1 = Rectangle(67, 69)
rect1.describe()
rect2 = Rectangle(6, 7)
rect2.describe()