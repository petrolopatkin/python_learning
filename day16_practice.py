#task1
from math_tools import a
from math_tools import b
from math_tools import add 
from math_tools import subtract
from math_tools import multiply
from math_tools import divide
print(add(a, b))
print(subtract(a, b))
print(multiply(a, b))
print(divide(a, b))
#task2
from greetings import say_hello
from greetings import ask_how_are_you
from greetings import say_goodbye
say_hello(name="Peter")
ask_how_are_you(name="Peter")
say_goodbye(name="Peter")
#task3
from geometry import length
from geometry import width
from geometry import height
from geometry import pi
from geometry import radius
from geometry import rectangle_area
from geometry import rectangle_perimeter
from geometry import circle_area
print(rectangle_area(length, width))
print(rectangle_perimeter(length, height))
print(circle_area(pi, radius))