length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
height = int(input("Enter a height: "))
pi = 3.14
radius = int(input("Enter a radius: "))
def rectangle_area(length, width):
    return length * width


def rectangle_perimeter(width, height):
    return 2 * (width + height)


def circle_area(pi, radius):
    return pi * radius ** 2