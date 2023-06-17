class QuizBrain:
    def __init__(self, new_question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = new_question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ").capitalize()
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, question_answer):
        if user_answer == question_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {question_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")

        # Just spacing between each question
        print("\n")
