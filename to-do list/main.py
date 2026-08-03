def show_task():
    with open("to-do list/tasks.txt", "r") as file:
        for line in file:
            print(line, end="")


def add_task():
    new_task = input("Enter a new task for today: ")
    with open("to-do list/tasks.txt", "a") as file:
        file.write(f"{new_task}\n")


def delete_task():
    number = 1
    with open("to-do list/tasks.txt") as file:
     tasks = file.readlines()
     if len(tasks) == 0:
         print("There are no tasks yet")
         return
     for task in tasks:
        print(f"{number}. {task}", end="")
        number += 1
    print()
    del_task = int(input("Which task you want to delete? "))
    if del_task < 1 or del_task > len(tasks):
     print("Invalid number, try again")
     return
    tasks.pop(del_task - 1)
    print("Task was successfully deleted\n")
    with open("to-do list/tasks.txt", "w") as file:
        for task in tasks:
            file.write(task)
    show_task()


def reset_tasks():
   with open("to-do list/default_tasks.txt", "r") as source:
    with open("to-do list/tasks.txt", "w") as file:
        for line in source:
            file.write(line)
    show_task()
      
       

while True:
    print("""
1. Show task
2. Add task
3. Delete task
4. Reset all tasks
5. Exit """)
    try:
        command = int(input("> "))
    except ValueError:
        print("Invalid value, try again!")
        continue
    if command == 1:
        show_task()
    elif command == 2: 
        add_task()
    elif command == 3:
        delete_task()
    elif command == 4:
        reset_tasks()
    elif command == 5:
        break
    else:
        print("Invalid command, try again")