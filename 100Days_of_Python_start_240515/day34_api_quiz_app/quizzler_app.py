from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import UI
import googletrans
import html

translater =googletrans.Translator()

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_korean = translater.translate(question_text,dest='ko').text # 한국어로 번역
    Encoded_q_text = html.unescape(question_korean) # 특수기호 문자열로 변경
    question_answer = question["correct_answer"]
    new_question = Question(Encoded_q_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

ui = UI(quiz)

