from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
QUIZ_COLOR = 'white'
WRONG_COLOR = 'red'
CORRECT_COLOR = 'green'

WIN_PAD_X = 20
WIN_PAD_Y = 20
QUIZ_PAD_Y = 30

QUIZ_WIDTH = 300
QUIZ_HEIGHT = 250
QUIZ_TEXT_WIDTH =280

TIME_RESULT_SHOW_MS = 500

SCORE_FONT = ('Arial', 10, 'bold')
SCORE_FONT_COLOR = 'white'
QUIZ_FONT = ('맑은 고딕', 18, 'bold')

BTN_BOLDER = 1
BTN_RELIEF = 'flat'

TRUE_IMG_PATH = "./images/true.png"
FALSE_IMG_PATH = "./images/false.png"


class UI():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=WIN_PAD_X, pady=WIN_PAD_Y, bg=THEME_COLOR)

        TRUE_IMG = PhotoImage(file=TRUE_IMG_PATH)
        FALSE_IMG = PhotoImage(file=FALSE_IMG_PATH)
        self.btn_true = Button(image=TRUE_IMG, bd=BTN_BOLDER, highlightthickness=0, command=self.Ture_select)
        self.btn_false = Button(image=FALSE_IMG, bd=BTN_BOLDER, highlightthickness=0, command=self.False_select)
        self.canvas_quiz = Canvas(width=QUIZ_WIDTH, height=QUIZ_HEIGHT, bg=QUIZ_COLOR)
        self.lbl_quiz = self.canvas_quiz.create_text(QUIZ_WIDTH / 2, QUIZ_HEIGHT / 2, width=QUIZ_TEXT_WIDTH,
                                                     font=QUIZ_FONT, text="quiz content", fill=THEME_COLOR)
        self.lbl_score = Label(text=f"Score :  0", font=SCORE_FONT, bg=THEME_COLOR, fg=SCORE_FONT_COLOR)

        self.place()
        self.next_quiz()
        self.window.mainloop()

    def place(self):
        self.lbl_score.grid(row=1, column=2)
        self.canvas_quiz.grid(row=2, column=1, columnspan=2, pady = QUIZ_PAD_Y)
        self.btn_true.grid(row=3, column=1)
        self.btn_false.grid(row=3, column=2)

    def Ture_select(self):
        self.show_result('True')

    def False_select(self):
        self.show_result('False')

    def return_quiz(self):
        self.canvas_quiz.config(bg=QUIZ_COLOR)
        self.next_quiz()


    def show_result(self,answer:str):
        if self.quiz.check_answer(answer) :
            self.canvas_quiz.config(bg=CORRECT_COLOR)
        else :
            self.canvas_quiz.config(bg=WRONG_COLOR)
        self.lbl_score.config(text=f'Score : {self.quiz.score}')
        self.window.after(TIME_RESULT_SHOW_MS,self.return_quiz)


    def next_quiz(self):
        if self.quiz.still_has_questions():
            self.canvas_quiz.itemconfig(self.lbl_quiz,text = self.quiz.next_question())
        else :
            self.end = True
            msg =f"퀴즈를 모두 푸셨습니다.\n\n최종 스코어 : {self.quiz.score}/{self.quiz.question_number}"
            self.canvas_quiz.itemconfig(self.lbl_quiz,text = msg)
            self.btn_true.config(state='disable')
            self.btn_false.config(state='disable')
