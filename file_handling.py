#Open a text file

with open("shopping.list.txt", "r") as file:
    for line in file:
        print(line, end="")
#Writing in a text file

with open("test_file.txt", "w") as file:
    file.write("Hello, , my name is Peter. I am 18 years old")

#Add some information into text file

with open("test_file.txt", "a") as file:
    file.write("\n I study English every day")
