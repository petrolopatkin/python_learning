#Task1
i = 1
while i <= 10:
    print(i)
    i = i + 1
#Task2
i = 10
while i >= 1:
    print(i)
    i = i - 1
#Task3
number = int(input("Enter a number "))
i = 1
while number >= i:
    print(i)
    i = i + 1
#Task4
password = "hakunamatata"
guess = input("Enter a password ")
while guess != password:
    print("Your password is incorrect")
    guess = input("Enter a password ")
    if guess == password:
        print("Your password is correct")
        break
#Task5
i = 0
number2 = int(input("Enter a number "))
while i <= number2:
    print(i)
    i = i + 1
    if i > number2:
        print("Go")
        break