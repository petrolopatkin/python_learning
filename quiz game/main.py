quiz = {
    "What is the capital of Germany?": "Berlin",
    "How many days are there in a week?": "7",
    "Which language is spoken in Brazil?": "Portuguese",
    "How many continents are there in the world?": "6"
}

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
       score = 0
       for question in quiz:
          print(question)
          answer = input("Answer: ")
          if answer == quiz[question]:
           print("Correct!")
           score += 1
          elif answer != quiz[question]:
           print("Incorrect!")
           score += 0 
       print(f"{score}/{len(quiz)}")
       percent = (score / len(quiz)) * 100
       print(percent)
       if percent == 100:
          print("Outstanding! You have reached a perfect score, congrats!")
       elif percent >= 80:
          print("Excellent! You are almost there!")
       elif percent >= 60:
          print("Good job!")
       elif percent < 60:
          print("Keep practicing! You will do better next time!")
    elif command == 2:
        question = input("Question: ")
        answer = input("Answer: ")
        item = question
        quiz[item] = answer
    elif command == 3:
       for question in quiz:
           print(f"""{question}
- {quiz[question]}""")
    elif command == 4:
        break
    else:
        print("Wrong command, try again")