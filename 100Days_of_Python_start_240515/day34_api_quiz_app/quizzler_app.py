from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import googletrans
import html

translater =googletrans.Translator()

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_korean = translater.translate(question_text,dest='ko').text # 한국어로 번역
    Encoded_q_text = html.unescape(question_korean) # 특수기호 문자열로 변경
    question_answer = question["correct_answer"]
    new_question = Question(question_korean, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
