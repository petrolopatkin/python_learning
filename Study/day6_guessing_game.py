secret_number = 9
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input("Take a guess "))
    guess_count += 1
    if guess == secret_number:
        print("Congrats, you've won")
        break
else:
    print("Sorry, you've lost")
