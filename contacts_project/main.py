contacts = {
    "Peter": "123456789",
    "Kate": "987654321"
}
def add_contact():
     name = input("Name: ")
     phone = input("Phone: ")
     item = name
     contacts[item] = phone


def find_contact():
     find_name = input("Name: ")
     if find_name in contacts:
      print(find_name , contacts[find_name])
     else:
      print("Contact not found")


def show_contacts():
  for item in contacts:
   print(item, contacts[item])


def delete_contact():
 delete_name = input("Name: ")
 if delete_name in contacts:
  contacts.pop(delete_name)


command = ""
while True:
  print("""
 1. Add contact
 2. Find contact
 3. Show all contacts
 4. Delete contact
 5. Exit
 """)
  try:
   command = int(input("> "))
  except ValueError:
     print("Invalid value, try again")
     continue
  if command == 1 :
        add_contact()
        print("Contact successfuly added!")
  elif command == 2 :
       find_contact()
  elif command == 3 :
       show_contacts()
  elif command == 4 :
       delete_contact()
       print("Contact was succssesfuly deleted")
  elif command == 5 :
       break
  else:
     print("You've entered wrong command, try again!")
