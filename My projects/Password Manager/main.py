import os

def clear():
   os.system("cls")


def show_password():
   with open("My projects/Password Manager/passwords.txt", "r") as file:
      for line in file:
         website, login, password = line.split("|")
         print(f"""===========================
Website: {website}
Login: {login}
Password: {password}
===========================""")


def add_password():
   website = input("What website you want to choose? ")
   login = input("Enter your login: ")
   password = input("Enter your password: ")
   with open("My projects/Password Manager/passwords.txt", "a") as file:
      file.write(f"{website}|{login}|{password}\n")
   print("Password successfully added!")


def search_website():
   pass


def delete_password():
   pass


while True:
    print("""
1. Show password
2. Add password
3. Search website
4. Delete password
5. Exit""")
    try:
     command = int(input("> "))
    except ValueError:
       print("Incorrect command, try again!")
       continue
    if command == 1:
       show_password()
       input("Click ENTER to continue")
       clear()
    elif command == 2:
       add_password()
       input("Click ENTER to continue")
       clear()
    elif command == 3:
       search_website()
       input("Click ENTER to continue")
       clear()
    elif command == 4:
       delete_password()
       input("Click ENTER to continue")
       clear()
    elif command == 5:
       break
    else:
       print("You have entered wrong command, please try again")