#Task1
temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
#Task2
name = "Peter"
if len(name) < 3:
    print("Name must be at least 3 charachters")
elif len(name) > 50:
    print("Name can be maximum of 50 charachters")
else:
    print("Name looks good!")
#Task3
number1 = int(input("Please, enter a first number "))
number2 = int(input("Please, enter a second number "))
if number1 > number2:
    print("First number is greater")
elif number2 > number1:
    print("Second number is greater")
else:
    print("Numbers are equal")
#Task4
age = int(input("Please, enter your age "))
if age < 18:
    print("You're  minor")
else:
    print("You're an adult")
#Task5
temperature2 = int(input("Please, enter a temperature right now "))
if temperature2 <= 0:
    print("It's freezing outside")
elif temperature2 < 20:
    print("It's cold outside")
elif temperature2 < 30:
    print("It's warm outside")
elif temperature2 >= 30:
    print("It's hot outside")
#Task5 
password = input("Please, enter a password ")
username = input("Please, enter a username ")
password == "hakunamatata"
username == "metallicatop"
if password == "hakunamatata" and username == "metallicatop":
    print("You're welcome!")
else:
    print("Wrong username or password, please try again")
#Task6
number = int(input("Please, enter your score "))
if number < 60:
    print("Your score is F, please try a test again")
elif number > 60 and number <= 70:
    print("Your score is D, not bad but I know you can do better")
elif number > 70 and number <= 80:
    print("Your score is C, good job!")
elif number > 80 and number <= 90:
    print("Your score is B, great job!")
elif number > 90 and number <= 100:
    print("Your grade is A, excellent!")