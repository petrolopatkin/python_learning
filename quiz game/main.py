import random
quiz = {
    "Geography":{
    "What is the capital of Germany?": "Berlin",
    "What is the capital of France?": "Paris",
    "What is the name of the longest river in the World?": "Amazon",
    "What is the capital of Great Britain?": "London",
    "What is the second longest river in the World?": "Nile"},
    "General knowledge": {
    "How many days are there in a week?": "7",
    "Which language is spoken in Brazil?": "Portuguese",
    "How many continents are there in the world?": "6",
    "How many days are there in the year?": "365",
    "Which language is spoken in China?": "Mandarin"},
    "Math":{
    "What is 7 * 6?": "42",
    "What is 63 / 9?": "7",
    "What is 3 ** 4?": "81",
    "What is 32 * 3?": "96",
    "What is 68 - 1?": "67"}
}
def start_quiz():
   selected_category = choose_category()
   questions = {}
   if selected_category == "All":
     for category in quiz:
       for question in quiz[category]:
         questions[question] = quiz[category][question]
   else:
     questions = quiz[selected_category]
   questions_list = list(questions)
   random.shuffle(questions_list)
   score = 0
   question_number = 1
   for question in questions_list:
    print(f"""=========================
 Question {question_number} of {len(questions_list)}
=========================
{question}""")
    question_number += 1
    answer = input("Answer: ")
    if answer == questions[question]:
     print("Correct!")
     score += 1
    elif answer != questions[question]:
     print(f"""Incorrect!
Correct answer was: {questions[question]} """)
   print(f"{score}/{len(questions_list)}")
   percent = (score / len(questions_list)) * 100
   print(f"{percent: .1f}%")
   if percent >= 100:
    print("Outstanding! You have reached a perfect score, congrats!")
   elif percent >= 80:
    print("Excellent! You are almost there!")
   elif percent >= 60:
    print("Good job!")
   elif percent < 60:
    print("Keep practicing! You will do better next time!")


def add_question():
   category = choose_category()
   questions = quiz[category]
   question = input("Question: ")
   answer = input("Answer: ")
   questions[question] = answer
   print("Question successfuly added")


def show_questions():
   selected_category = choose_category()
   if selected_category == "All":
     for category in quiz:
      print(category)
      questions = quiz[category]
      for question in questions:
       print(f"""==================================================
{question}
==================================================""")
       print(f"- {questions[question]}")
   else:
     questions = quiz[selected_category]
     for question in questions:
      print(f"""{question}
- {questions[question]}""")
   

def choose_category():
  print("""Choose category:
1. Geography
2. General knowledge
3. Math
4. All categories""")
  choice =  int(input("> "))
  if choice == 1:
    return "Geography"
  elif choice == 2:
    return "General knowledge"
  elif choice == 3:
    return "Math"
  elif choice == 4:
    return "All"


def delete_question():
  number = 1
  selected_category = choose_category()
  if selected_category == "All":
    for category in quiz:
       for question in quiz[category]:
        print("Delete question is available only inside one category!")
        return
  questions = quiz[selected_category]
  questions_list = list(questions)
  for question in questions:
     print(f"{number}. {question}")
     number += 1
  del_question = int(input("Select a question to delete: "))
  if del_question < 1 or del_question > len(questions_list):
    print("Invalid number, try again")
    return
  selected_question = questions_list[del_question - 1]
  if selected_question in questions_list:
   questions.pop(selected_question)
   print("Question successfuly deleted") 
      
def edit_question_or_answer():
  number = 1
  category = choose_category()
  questions = quiz[category]
  questions_list = list(questions)
  for question in questions:
    answer = questions[question]
    print(f"{number}. {question}")
    print(f"- {answer}")
    number += 1
  select_q = int(input("Select: question: "))
  if select_q < 1 or select_q > len(questions_list):
    print("Invalid number, try again")
    return
  selected_question = questions_list[select_q - 1]
  edit_q_or_a = int(input("""What do you want to edit?: 
  1. Question
  2. Answer """))
  if edit_q_or_a < 1 or edit_q_or_a > 2:
    print("Invalid number, try again")
  if edit_q_or_a == 1:
    new_q = (input("New question: "))
    questions[new_q] = questions[selected_question]
    if selected_question in questions_list:
     questions.pop(selected_question)
  if edit_q_or_a == 2:
    new_a = (input("New answer: "))
    questions[selected_question] = new_a
  print("Question successfuly changed")

while True:
    print("""
1. Start quiz
2. Add question
3. Edit question or answer
4. Show all questions
5. Delete question
6. Exit
""")
    try:
     command = int(input("> "))
    except ValueError:
        print("Invalid value")
        continue
    if command == 1:
       start_quiz()
    elif command == 2:
        add_question()
    elif command == 3:
       edit_question_or_answer()
    elif command == 4:
        show_questions()
    elif command == 5:
        delete_question()
    elif command == 6:
      break
    else:
        print("Wrong command, try again")