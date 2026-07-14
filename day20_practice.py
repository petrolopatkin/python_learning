#task1
students = {
    "Peter": 99,
    "Kate": 95,
    "Jhon": 67
}
def add_student():
 name = input("Name: ")
 grade = int(input("Grade: "))
 item = name
 students[item] = grade


def find_student():
   find_name = input("Name: ")
   if find_name in students:
      print(students[find_name])
   else:
      print("Student not found")


def show_students():
   for item in students:
      print(item, students[item])


def delete_student():
   delete_name = input("Name: ")
   if delete_name in students:
      students.pop(delete_name)
      print("Student deleted")
   else:
      print("Student not found")


while True:
    print("""
1. Add student
2. Find student
3. Show all students
4. Delete student
5. Exit
 """)
    command = int(input("> "))
    if command == 1:
       add_student()
    elif command == 2:
       find_student()
    elif command == 3:
       show_students()
    elif command == 4:
       delete_student()
    elif command == 5:
       break
    else:
       print("This command doesn't exist, try again")
    