library = {
    "Peter": ["Football Manager 24", "Detroid: Become a Human", "Silent Hill 2"],
    "Kate": ["Minecraft", "Resident Evil 4"]
}
command = " "
while True:
    print("""
1. Add user
2. Add game
3. Show library
4. Delete game
5. Exit
 """)
    try:
     command = int(input("> "))
    except(ValueError):
       print("Invalid value, try again")
       continue
    if command == 1:
        add_user = input("Username: ")
        if add_user not in library:
           library[add_user] = []
           print(add_user, library[add_user])
        elif add_user in library:
            print("User is already in library")
    elif command == 2:
        add_user = input("Username: ")
        if add_user not in library:
           print("User not found")
        elif add_user in library:
         add_game = input("Game: ")
         library[add_user].append(add_game)
         print("Game succssesfuly added")
    elif command == 3:
       for user in library:
          print(user)
          for game in library[user]:
           print(f"- {game}")
    elif command == 4:
       delete_game = input("Game: ")
       for user in library:
          library[user]
          if delete_game in library[user]:
             library[user].remove(delete_game)
             print("Game succssesfuly deleted")
    elif command == 5:
        break
    else:
     print("Command is wrong, try again")