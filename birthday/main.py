import time
def slow_print(message):
   for letter in message:
      print(letter, end="")
      time.sleep(0.05)
   print()


def intro():
    intro_message = """========================================================================================
      🎉С Днем рождения!!🎉
Привет, Пап. Сегодня я подготовил для тебя небольшое представление в честь дня рождения 
Нажми на ENTER, чтобы продолжить.
========================================================================================"""
    slow_print(intro_message)
    input()

def first_scene():
    while True:
     first_scene_message = """=============================================
Перед тобой появилась подарочная коробка 🎁
Что бы ты хотел с ней сделать?
1. Открыть сразу
2. Потрясти коробку
============================================="""
     slow_print(first_scene_message)
     try:
      choice = int(input("> "))
     except ValueError:
        print("Invalid value, try again")
        continue
     if choice == 1:
      choice1 = """
Ты слишком торопишься. 
Так представление будет не интересным.
Попробуй другой вариант.
"""
      slow_print(choice1)
     elif choice == 2:
      choice2 = """
Ты потряс коробку...
Внутри ощущаеться что-то тяжелое
Что же это может быть?
"""
      slow_print(choice2)
      break



def second_scene():
    while True:
        second_scene_message = """================================================
Ты поставил коробку на место.
Осмотрев ее перед тобой появились 3 возможности.
1. Приоткрыть коробку
2. Попробовать заглянуть в щель
3. Продолжить представление
================================================
"""

        slow_print(second_scene_message)
        try:
            choice = int(input("> "))
        except ValueError:
            print("Invalid value, try again")
            continue
        if choice == 1:
            open_box = "Все еще слишком рано! Попробуй выбрать другой вариант."
            slow_print(open_box)
        elif choice == 2:
            try_to_look_into = "Внутри коробки слишком темно, ничего не видно."
            slow_print(try_to_look_into)
        elif choice == 3:
            continue_show = "Отлично, правильный выбор. Продолжаем представление."
            slow_print(continue_show)
            break
        else:
            print("Ты выбрал неправильный вариант, попробуй снова")


def third_scene():
   while True:
      third_scene_message = """=============================================================
Чтобы открыть коробку тебе понадобиться какой-то инструмент
Какой же инструмент ты выберешь?
1. Попробовать открыть молотком
2. Проделать дыру дрелью
3. Использовать универсальную открывашку
============================================================="""
      slow_print(third_scene_message)
      try:
         choice = int(input("> "))
      except ValueError:
         print("Invalid value, try again")
         continue
      if choice == 1:
         choice1 = """Ты выбрал молоток.
После одного сильного удара коробка разлетаеться в дребезги..
Вместе с подарком..
Попробуй выбрать другой вариант
"""
         slow_print(choice1)
      elif choice == 2:
         choice2 = """Ты выбрал дрель
Ты попробовать просверлить дырку в коробке..
Но не расчитал силы и пробил ее..
Вместе с подарком и столом..
Я думаю стоит попробовать другой вариант
"""
         slow_print(choice2)
      elif choice == 3:
         choice3 = """Ты выбрал универсальную открывашку.
После пары неудачных попыток у тебя получилось открыть коробку.
И внутри..
Еще одна коробка;)
"""
         slow_print(choice3)
         break
      else:
         print("Ты выбрал неправильный вариант, попробуй снова")

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
        third_scene()
        last_scene()
    elif command == 2:
        break
    else:
        print("Invalid command, try again")