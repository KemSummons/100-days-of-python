from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for elem in question_data:
    question_text = elem['text']
    question_answer = elem['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz. \nYour final score was: {quiz.score}/{quiz.question_number}.")
