#Task1
for x in range(4):
    for y in range(2):
        print(f'({x}, {y})')
#Task2
numbers = [5, 2, 5, 2, 2]
for item in numbers:
    output = ''
    for count in range(item):
        output += '*'
    print(output)
#Task3
numbers2 = [1, 1, 1, 1, 5]
for item2 in numbers2:
    result = ''
    for count in range(item2):
        result += '@'
    print(result)