from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]

    new_q = Question(question_text, question_answer)

    question_bank.append(new_q)

new_quiz_brain = QuizBrain(question_bank)

while new_quiz_brain.still_has_questions():
    new_quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {new_quiz_brain.score}/{len(question_bank)}")