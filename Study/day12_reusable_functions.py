def convert(message):
    emoji = {
        ":)": "😊",
        ":(": "😞"
    }
    for item in emoji:
        message = message.replace(item, emoji[item])    
    return message


message = input("> ")
print(convert(message))