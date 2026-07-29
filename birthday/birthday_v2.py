import time
from PIL import Image
import pygame
pygame.mixer.init()
magic_appearance = pygame.mixer.Sound("birthday/sounds/magic_appearance.wav")
magic_appearance2 = pygame.mixer.Sound("birthday/sounds/magic_appearance2.wav")
hammer = pygame.mixer.Sound("birthday/sounds/hammer_hit.wav")
drill =  pygame.mixer.Sound("birthday/sounds/drill_sound_new.wav")
second_box = pygame.mixer.Sound("birthday/sounds/appearance_for_second_box.wav")
wrong_answer = pygame.mixer.Sound("birthday/sounds/wrong_answer.wav")
correct_answer =  pygame.mixer.Sound("birthday/sounds/correct_answer.wav")
song = pygame.mixer.Sound("birthday/sounds/background_song.mp3")
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
    image1 = Image.open('birthday/pictures/test.jpg')
    slow_print(intro_message)
    time.sleep(1)
    magic_appearance.play()
    image1.show()
    input("Нажми ENTER чтобы продолжить ")
    time.sleep(2)

def first_scene():
    while True:
     first_scene_message = """=============================================
Перед тобой появилась подарочная коробка 🎁
Что бы ты хотел с ней сделать?
1. Открыть сразу
2. Потрясти коробку
============================================="""
     box_image = Image.open("birthday/pictures/birthday_box.jpg")
     slow_print(first_scene_message)
     time.sleep(1)
     magic_appearance2.play()
     box_image.show()
     try:
      choice = int(input("> "))
     except ValueError:
        print("Ты ввел несуществующий вариант, попробуй снова")
        continue
     if choice == 1:
      wrong_answer.play()
      choice1 = """
Ты слишком торопишься. 
Так представление будет не интересным.
Попробуй другой вариант.
"""
      slow_print(choice1)
     elif choice == 2:
      correct_answer.play()
      choice2 = """
Ты потряс коробку...
Внутри ощущаеться что-то тяжелое
Что же это может быть?
"""
      slow_print(choice2)
      time.sleep(2)
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
            print("Ты ввел несуществующий вариант, попробуй снова")
            continue
        if choice == 1:
            wrong_answer.play()
            open_box = "Все еще слишком рано! Попробуй выбрать другой вариант."
            slow_print(open_box)
        elif choice == 2:
            wrong_answer.play()
            try_to_look_into = "Внутри коробки слишком темно, ничего не видно."
            slow_print(try_to_look_into)
        elif choice == 3:
            correct_answer.play()
            continue_show = "Отлично, правильный выбор. Продолжаем представление."
            slow_print(continue_show)
            time.sleep(2)
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
         print("Ты ввел несуществующий вариант, попробуй снова")
         continue
      if choice == 1:
         choice1 = """Ты выбрал молоток.
После одного сильного удара коробка разлетаеться в дребезги..
Вместе с подарком..
Попробуй выбрать другой вариант
"""
         crushed_box1 = Image.open("birthday/pictures/crushed_box1.jpg")
         slow_print(choice1)
         time.sleep(1)
         hammer.play()
         crushed_box1.show()
      elif choice == 2:
         choice2 = """Ты выбрал дрель
Ты попробовал просверлить дырку в коробке..
Но не расчитал силы и пробил ее..
Вместе с подарком и столом..
Я думаю стоит попробовать другой вариант
"""
         crushed_box2 = Image.open("birthday/pictures/crushed_box2.jpg")
         slow_print(choice2)
         time.sleep(1)
         drill.play()
         crushed_box2.show()
      elif choice == 3:
         choice3 = """Ты выбрал универсальную открывашку.
После пары неудачных попыток у тебя получилось открыть коробку.
И внутри..
Еще одна коробка;)
"""
         box_in_box = Image.open("birthday/pictures/box_in_box.jpg")
         slow_print(choice3)
         time.sleep(1)
         magic_appearance.play()
         box_in_box.show()
         time.sleep(2)
         break
      else:
         print("Ты выбрал неправильный вариант, попробуй снова")
      


def fourth_scene():
   while True:
    fourth_scene_message = """=======================================================
Итак, теперь твоя задача открыть маленькую коробку
Выбери способ которым ты ее откроешь
1. Попробовать открывашку
2. Ударить молотком
3. Открыть руками
=======================================================
"""
    small_box = Image.open("birthday/pictures/small_box.jpg")
    slow_print(fourth_scene_message)
    time.sleep(1)
    second_box.play()
    small_box.show()
    try:
       choice = int(input("> "))
    except ValueError:
       print("Ты ввел несуществующий вариант, попробуй снова")
       continue
    if choice == 1:
       wrong_answer.play()
       choice1 = "В этот раз открывашка не подходит. Попробуй другой вариант"
       slow_print(choice1)
    elif choice == 2:
       wrong_answer.play()
       choice2 = "Предыдущий опыт тебя ничему не учит? Ты снова сломал коробку. Попробуй другой вариант"
       slow_print(choice2)
    elif choice == 3:
       correct_answer.play()
       choice3 = "Небольшой троллинг)) С этой коробкой все намного проще чем с первой"
       slow_print(choice3)
       time.sleep(2)
       break
    else:
       print("Ты выбрал неправильный вариант, попробуй снова")
    


def last_scene():
   while True:
    song.play()
    last_scene_message1 = """==============================================================================================
Поздравляю, ты дошел до финальной сцены моего небольшого шоу
Надеюсь это было хоть чуточку весело, потому что мне было очень сложно придумать что-то самому
==============================================================================================
"""

    slow_print(last_scene_message1)
    time.sleep(1)

    last_scene_message2 = """===============================================================================================================================================
Пап, поздравляю тебя с днем рождения!
Желаю, чтобы в жизни было побольше радостных моментов.
Чтобы здоровье не подводило тебя в важные моменты.
Чтобы получалось все задуманное, а все мечты ставали целями.
Ты сделал очень много в жизни для меня и для нашей семьи в целом, спасибо тебе большое.
Надеюсь, что в ближайших пару лет я смогу вам помогать, чтобы вы с мамой просто сидели дома и отдыхали.
Спасибо, что сыграл в мою маленькую игру, я правда над ней старался.
Можешь считать, что в нее вложены очень многие знания, которые я получил за время моих занятий.
Пока мне нравиться это дело и я планирую продолжать развиваться в этой сфере.
Если у тебя появятся идеи как сделать эту игру ещё лучше — обязательно расскажи мне. 
Мне очень интересно развиваться и делать проекты более качественными.
Еще раз с днем рождения и хорошего дня!
===============================================================================================================================================
"""
    slow_print(last_scene_message2)
    input("Нажми на ENTER, чтобы закрыть проект ")
    break


while True:
    print("""
1. Start
2. Exit""")
    try:
        command = int(input("> "))
    except ValueError:
        print("Ты ввел несуществующий вариант, попробуй снова")
        continue
    if command == 1:
        intro()
        first_scene()
        second_scene()
        third_scene()
        fourth_scene()
        last_scene()
    elif command == 2:
        break
    else:
        print("Ты ввел неправильную команду, попробуй снова")