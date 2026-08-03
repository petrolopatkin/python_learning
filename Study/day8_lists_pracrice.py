#task1
fruits = ['Banana', 'Apple', 'Orange', 'Mandarin', 'Pineapple']
fruits[1] = 'Mango' 
print(fruits[0:])
#task2
numbers = [25, 8, 30, 3, 1]
total = 0
for item in numbers:
    total += item
print(f'Total: {total}')
#task3 
names = ['Peter' , 'John', 'Stacy', 'William', 'Morgan']
for item in names:
    print(item)
#task4
numbers2 = [40, 67, 69, 52]
number = int(input('Enter a number '))
if number in numbers2:
    print('Found')
else:
    print('Not found')