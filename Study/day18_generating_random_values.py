import random

for item in range(3):
    print(random.randint(10, 20))


members = ["Jhon", "Peter", "Kate", "Mosh", "Micheal", "Daniel"]
leader = random.choice(members)
print(f"Leader: {leader}")
#task roll the dice

class Dice:
    def roll(self):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        return a, b
    

dice = Dice()
print(dice.roll())