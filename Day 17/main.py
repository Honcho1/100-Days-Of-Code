from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = [
    Question(html.unescape(question["question"]), question["correct_answer"])
    for question in question_data["results"]
]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz. Your final score is: {quiz.score}/{len(question_bank)}")