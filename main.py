from data import question_data

score = 0
question_number = 0

for i in range (len(question_data)):
    question_text = question_data[i]["question"]
    question_answer = question_data[i] ["correct_answer"]
    question_number += 1
    user_answer = input(f"Q{question_number}: {question_text} True or false: ").lower()
    if user_answer == question_answer.lower():
        score += 1
        print("That's correct!")
    else:
        print(f"Incorrect. The correct answer was {question_answer.lower()}.")
    if i == (len(question_data))-1:
        print("You've completed the quiz!")
        print(f"your final score is {score}")