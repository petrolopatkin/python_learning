#task1
coordinates = (67, 69)
x, y = coordinates
print(x, y)
#task2
numbers = [10, 20, 60]
one, two, three = numbers
total = 0
for item in numbers:
    total += item
print(f'Total: {total}')
#task3+4+5
person = {
    "name": "Peter",
    "age": 18,
    "city": "Presov"
}
person ["job"] = "Programmer"
key = input("Enter a key: ").lower()
if key in "age":
    print(person["age"])
else:
    print("Key not found")
#task 6
students = {
    "Petyr": 100,
    "Jhon":  67,
    "Mary": 69,
    "Elton": 52,
    "Daniel": 99
}
for item in students:
    print(item, students[item])
#task 7
fruits = {
    "Apple": 100,
    "Banana": 150,
    "Orange": 125,
    "Papaya": 300,
    "Kiwi": 185,
    "Pineapple": 90
}
highest_price = 0
highest_item = " "
for item in fruits:
 price = fruits[item]
 if price > highest_price:
    highest_price = price
    highest_item = item
print(highest_item, highest_price)
#task8
invertory = {
   "Keyboard": 6,
   "Headphones": 10,
   "Mouse": 7,
   "Monitor": 4
}
total = 0
for item in invertory:
   total += invertory[item]
print(f"Total: {total}")