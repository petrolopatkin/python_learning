import os

def clear():
   os.system("cls")


def show_password():
   with open("My projects/Password Manager/passwords.txt", "r") as file:
      for line in file:
         line = line.strip()
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
   website = input("Enter a website: ")
   with open("My projects/Password Manager/passwords.txt", "r") as file:
      for line in file:
         line = line.strip()
         saved_website, login, password = line.split("|")
         if website == saved_website:
            print(f"""===========================
Website: {saved_website}
Login: {login}
Password: {password}
=========================== """)
            return
      else:
       print("Website not found")


def delete_password():
   with open("My projects/Password Manager/passwords.txt", "r") as file:
      password = file.readlines()
      if not password:
         print("There are no passwords yet")
         return
      number = 1
      for website in password:
         print(f"{number}. {website}", end="\n")
         number += 1
      print()
      del_password = int(input("Which password you want to delete? "))
      if del_password < 1 or del_password > len(password):
         print("Invalid number, try again")
         return
      while True:
       warning_message = input("Are you sure you want to delete this password? ").lower()
       if warning_message == 'y':
            password.pop(del_password - 1)
            print("Password was successfuly deleted")
            break
       elif warning_message == 'n':
            print("You have canceled deletion")
            return
       else:
            print("You have picked incorrect option")
            continue
      with open("My projects/Password Manager/passwords.txt", "w") as file:
          for website in password:
             file.write(website)
   show_password()
            

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
       input("Click ENTER to continue ")
       clear()
    elif command == 2:
       add_password()
       input("Click ENTER to continue ")
       clear()
    elif command == 3:
       search_website()
       input("Click ENTER to continue ")
       clear()
    elif command == 4:
       delete_password()
       input("Click ENTER to continue ")
       clear()
    elif command == 5:
       break
    else:
       print("You have entered wrong command, please try again")