#Task1
for item in range(11):
    print(item)
#Task2
for item in range(10,0, -1):
    print(item)
#Task3 
number = int(input("Enter a number: "))
for item in range(1, number+1, 1):
    print(item)
#Task4
for item in range(5):
    for item in ['****']:
     print(item)
#Task5
for item in range(1, 6):
   print('*' * item)
#Task6
total = 0
for item in range(1, 101):
   total = total + item
   print(f"Total: {total}")