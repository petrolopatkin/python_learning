contacts = {
    "Peter": "123456789",
    "Kate": "987654321"
}
command = ""
while True:
  print("""
 1. Add contact
 2. Find contact
 3. Show all contacts
 4. Delete contact
 5. Exit
 """)
  command = int(input("> "))
  if command == 1 :
        name = input("Name: ")
        phone = input("Phone: ")
        item = name
        contacts[item] = phone
  elif command == 2 :
       find_name = input("Name: ")
       if find_name in contacts:
            print(contacts[find_name])
       else:
            print("Contact not found")
  elif command == 3 :
       for item in contacts:
            print(item, contacts[item])
  elif command == 4 :
       delete_name = input("Name: ")
       if delete_name in contacts:
            contacts.pop(delete_name)
       else:
            print("Contact not found")
  elif command == 5 :
       break
  else:
       print("You've entered wrong command, try again")
    
