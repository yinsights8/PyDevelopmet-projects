class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_num = 0
        self.score = 0

    def still_has_question(self):
        total_question = len(self.question_list)
        # return true until the condition becomes false
        # 1 != 12 == True
        if total_question != self.question_num:
            return True
        else:
            # when the 12 != 12 == False
            return False

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q{self.question_num}. {current_question.text} (True/False): ")

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_num}")
        print("\n")

