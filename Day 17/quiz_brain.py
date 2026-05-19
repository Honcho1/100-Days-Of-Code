class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
        return user_answer
    
    def check_answer(self, user_answer):
        current_question = self.question_list[self.question_number]
        is_correct = user_answer.strip().title() == current_question.answer
        if is_correct:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {current_question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n")
        return is_correct
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
