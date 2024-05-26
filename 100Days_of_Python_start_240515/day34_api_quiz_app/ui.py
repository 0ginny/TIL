from tkinter import *

THEME_COLOR = "#375362"
QUIZ_COLOR = 'white'

WIN_PAD_X = 20
WIN_PAD_Y = 20
QUIZ_PAD_Y = 30

QUIZ_WIDTH = 300
QUIZ_HEIGHT = 250

SCORE_FONT = ('Arial', 10, 'bold')
SCORE_FONT_COLOR = 'white'
QUIZ_FONT = ('Arial', 20, 'italic')

BTN_BOLDER = 1
BTN_RELIEF = 'flat'

TRUE_IMG_PATH = "./images/true.png"
FALSE_IMG_PATH = "./images/false.png"


class UI():
    def __init__(self,quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=WIN_PAD_X, pady=WIN_PAD_Y, bg=THEME_COLOR)

        TRUE_IMG = PhotoImage(file=TRUE_IMG_PATH)
        FALSE_IMG = PhotoImage(file=FALSE_IMG_PATH)
        self.btn_true = Button(image=TRUE_IMG, bd=BTN_BOLDER, highlightthickness=0)
        self.btn_false = Button(image=FALSE_IMG, bd=BTN_BOLDER, highlightthickness=0)
        self.canvas_quiz = Canvas(width=QUIZ_WIDTH, height=QUIZ_HEIGHT, bg=QUIZ_COLOR)
        self.lbl_quiz = self.canvas_quiz.create_text(QUIZ_WIDTH / 2, QUIZ_HEIGHT / 2,
                                                     font=QUIZ_FONT, text="quiz content", fill=THEME_COLOR)
        self.score = 0
        self.lbl_score = Label(text=f"Score : {self.score}", font=SCORE_FONT, bg=THEME_COLOR, fg=SCORE_FONT_COLOR)

        self.place()

        self.window.mainloop()

    def place(self):
        self.lbl_score.grid(row=1, column=2)
        self.canvas_quiz.grid(row=2, column=1, columnspan=2, pady = QUIZ_PAD_Y)
        self.btn_true.grid(row=3, column=1)
        self.btn_false.grid(row=3, column=2)
