#task1
def greet():
    print("Hello!")
    print("Welcome to Python")


greet()
greet()
greet()
#task2
def say_hello(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")


say_hello("Peter", "Smith")
say_hello("Morgan", "Rogers")
#task3
def add(number1, number2):
    return number1 + number2


print(add(5, 7))
#task4
def is_even(number):
    if number % 2 is 0:
        print("Even")
    else:
        print("Odd")


is_even(7)
#task5
def rectangle_area(length, width):
    return length * width


print(rectangle_area(length=67, width=69))
#task6
numbers = [5, 15, 67, 8, 3, 10]
def find_largest(numbers):
    largest_number = numbers[0]
    for item in numbers:
        if item > largest_number:
            largest_number = item
    return largest_number


print(find_largest(numbers))
#task7
numbers5 = [2, 6, 15, 20, 36, 41, 45, 50, 100]
def even_count(numbers5):
    count = 0
    for item in numbers5:
        if item % 2 == 0:
            count += 1
    return count


print(even_count(numbers5))
#task8
message = " "
def convert(message):
    emoji = {
        ":)": "😊",
        ":(": "😞"
    }
    for item in emoji:
        message = message.replace(item, emoji[item])    
    return message


print(convert("Hello my dear :)"))