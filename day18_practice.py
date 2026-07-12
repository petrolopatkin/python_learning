import random
from pathlib import Path
#task1 coin
coin = ["Heads", "Tails"]
coin_drop = random.choice(coin)
print(f"You dropped: {coin_drop}")
#task2 Guess the number
number = int(input("Enter a number: "))
number1 = random.randint(1, 10)
if number == number1:
    print("Congrats! You've won")
else:
    print(f"You've lost!. The number was {number1}")
#task3 test folder
path = Path("test_folder")
path.exists()
if path.exists() == True:
    print("Folder exists")
else:
    print("Folder doesn't exist")
#task4 all files in python_learning
path = Path()
for file in path.glob("*"):
    print(file)
#task5 Dice roller
class Dice:
    def roll(self):
        print("You rolled:")
        print(random.randint(1, 6))


dice = Dice()
while True:  
    dice.roll()
    answer = input("Roll again? y/n: ").lower()
    if answer == "n":
        print("Goodbye!")
        break
    elif answer == "y":
        continue
    else:
        print("Incorrect value")
