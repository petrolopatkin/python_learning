import time
def intro():
    letter = """========================================================================================
      🎉С Днем рождения!!🎉
Привет, Пап. Сегодня я подготовил для тебя небольшое представление в честь дня рождения 
Нажми на ENTER, чтобы продолжить.
========================================================================================"""
    for text in letter:
     print(text, end="")
     time.sleep(0.05)

    print()
    input()

def first_scene():
    while True:
     letter = """=============================================
Перед тобой появилась подарочная коробка 🎁
Что бы ты хотел с ней сделать?
1. Открыть сразу
2. Потрясти коробку
============================================="""
     for text in letter:
      print(text, end="")
      time.sleep(0.05)

     print()
     try:
      choice = int(input("> "))
     except ValueError:
        print("Invalid value, try again")
        continue
     if choice == 1:
      letter2 = """======================================
Ты слишком торопишься. 
Так представление будет не интересным.
Попробуй другой вариант.
======================================"""
      for text2 in letter2:
       print(text2, end= "")
       time.sleep(0.05)
     elif choice == 2:
      letter3 = """=================================
Ты потряс коробку...
Внутри ощущаеться что-то тяжелое
Что же это может быть?
================================="""
      for text3 in letter3:
       print(text3, end="")
       time.sleep(0.05)

      print()
      break



def second_scene():
    while True:
        msg = """===========================================
Ты поставил коробку на место.
Осмотрев ее перед тобой появились 3 возможности.
1. Приоткрыть коробку
2. Попробовать заглянуть в щель
3. Продолжить представление
===========================================
"""

        for sdsc in msg:
            print(sdsc, end="")
            time.sleep(0.05)

        print()

        try:
            choice = int(input("> "))
        except ValueError:
            print("Invalid value, try again")
            continue

        if choice == 1:
            open_box = "Все еще слишком рано! Попробуй выбрать другой вариант."

            for message in open_box:
                print(message, end="")
                time.sleep(0.05)

            print()

        elif choice == 2:
            try_to_look_into = "Внутри коробки слишком темно, ничего не видно."

            for message in try_to_look_into:
                print(message, end="")
                time.sleep(0.05)

            print()

        elif choice == 3:
            continue_show = "Отлично, правильный выбор. Продолжаем представление."

            for message in continue_show:
                print(message, end="")
                time.sleep(0.05)

            print()
            break

        else:
            print("Wrong choice, try again.")


def last_scene():
    print("Last")


while True:
    print("""
1. Start
2. Exit""")
    try:
        command = int(input("> "))
    except ValueError:
        print("Incorrect value, try again")
        continue
    if command == 1:
        intro()
        first_scene()
        second_scene()
        last_scene()
    elif command == 2:
        break
    else:
        print("Invalid command, try again")