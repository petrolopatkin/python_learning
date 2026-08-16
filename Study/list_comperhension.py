# We use list comperhenstion to compact and easier read than traditional loops
#expression for value in iterable if condition
doubles = [x * 2 for x in range(1, 11) ]
triples = [y * 3 for y in range(1,11)]
squares = [z ** 2 for z in range(1,11)]
print(doubles)
print(triples)
print(squares)
# lists of strings
fruits = ["apple", "orange", "banana", "pomegranate", "pineapple"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)
# conditions
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_num = [num for num in numbers if num >= 0]
negative_num = [num for num in numbers if num < 0]
even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 == 1]
print(positive_num)
print(negative_num)
print(even_num)
print(odd_num)
# task
grades = [67, 99, 42, 52, 87, 44, 32, 66, 79, 95]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)