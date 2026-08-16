from dataclasses import dataclass
from dataclasses import field
#Book class
@dataclass
class Book:
    name: str
    author: str
    year: int
    amount_of_pages: int


    def read(self, pages):
        self.current_pages += pages


    def progress(self):
        return self.currecnt_progress ==  self.current_pages / 100


    def is_finished(self):
        return self.current_pages >= self.pages 

#Product class
@dataclass
class Product:
    category: str
    item: str
    quantity: int 
    price: float 

    def total_price(self):
        return self.quantity * self.price


    def availability(self):
        if self.quantity >= 1:
            print("Product is available")
        elif self.quantity == 0:
            print("Product is not available")
        else:
            print("Products's quantity can't be negative")


    def remove(self):
        buy = int(input("How many products you want ti buy? "))
        if buy > self.quantity:
         print("You can't buy more products than are available")
        else:
         print("Your purchase was successfull")
         self.quantity = self.quantity - buy
        

#class Student
@dataclass
class Student:
    name: str
    age: int
    grades: list[int]
    course: str

    def avg_grades(self):
        return sum(self.grades)/len(self.grades)


    def description(self):
        print(f"""
Name: {self.name}
Age: {self.age}
Grades: {self.grades}
Course: {self.course}""")


    def change_course(self, new_course):
        self.course = new_course


    def test_grades(self):
        passing_grades = [grade for grade in self.grades if grade >= 60]
        unpassing_grades = [grade for grade in self.grades if grade < 60]
        print(f"This student has a passing grades {passing_grades}")
        print(f"This student has unpassing grades {unpassing_grades}")
        passing_percentage = (len(passing_grades)/len(self.grades)) * 100
        if passing_percentage >= 60:
            print("Student has passed an exam")
        elif passing_percentage < 60:
            print("Student has failen an exam")


std1 = Student("John", 18, [80, 55, 75, 44, 80], "IT")
std1.test_grades()