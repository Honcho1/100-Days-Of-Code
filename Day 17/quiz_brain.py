class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
        return user_answer
    
    def check_answer(self, user_answer):
        current_question = self.question_list[self.question_number]
        return user_answer.strip().title() == current_question.answer
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    