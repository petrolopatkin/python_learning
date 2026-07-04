customer = {
    "Name": "Peter",
    "Age": 18,
    "Adress": "17.novembra",
    "Phone": "556998754",
    "is_verified": True
}
print(customer.get("birthday"))
#task1
phone = input("Phone: ")
phone_number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
output = ""
for character in phone:
    output += phone_number.get(character, '!') + " "
print(output)