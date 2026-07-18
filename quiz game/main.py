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
   category = choose_category()
   questions = quiz[category]
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
   print(percent)
   if percent == 100:
    print("Outstanding! You have reached a perfect score, congrats!")
   elif percent >= 80:
    print("Excellent! You are almost there!")
   elif percent >= 60:
    print("Good job!")
   elif percent < 60:
    print("Keep practicing! You will do better next time!")


def add_question():
   question = input("Question: ")
   answer = input("Answer: ")
   item = question
   quiz[item] = answer


def show_questions():
   for question in quiz:
    print(f"""{question}
- {quiz[question]}""")
    

def choose_category():
  print("""Choose category:
1. Geography
2. General knowledge
3. Math""")
  choice =  int(input("> "))
  if choice == 1:
    return "Geography"
  elif choice == 2:
    return "General knowledge"
  elif choice == 3:
    return "Math"


while True:
    print("""
1. Start quiz
2. Add question
3. Show all questions
4. Exit
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
       show_questions()
    elif command == 4:
        break
    else:
        print("Wrong command, try again")