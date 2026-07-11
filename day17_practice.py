#task1
from math_utils import operations
give_number = int(input("Enter a number: "))
print(operations.square(give_number))
print(operations.cube(give_number))
#task2
from school import students
student1 = students.Student("Peter", 18)
student2 = students.Student("Kate", 17)
student1.introduce()
student2.introduce()
from shop import products
products.show_products()