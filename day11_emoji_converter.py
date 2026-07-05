message = input("> ")
words = message.split(' ')
emoji = {
    ":)": "😊",
    ":(": "😞"
}
output = ""
for item in words:
    output += emoji.get(item, item) + " "
print(output)