from tkinter import *
import pandas as pd
import random as rd

# color
BACKGROUND_COLOR = "#B1DDC6"

# window feature
TITLE = 'Flashy'
RESIZABLE = False

# image path
BACK_CARD_PATH = './images/card_back.png'
FRONT_CARD_PATH = './images/card_front.png'
RIGHT_IMG_PATH = './images/right.png'
WRONG_IMG_PATH = './images/wrong.png'

# features size
WIN_WIDTH = 800
WIN_HEIGHT = 526
WIN_PAD_X = 50
WIN_PAD_Y = 50

CARD_WIDTH = 800
CARD_HEIGHT = 526

POS_EN_X = 400
POS_EN_Y = 150
POS_KO_X = 400
POS_KO_Y = 263

# font
FONT_LANGUAGE = ('Arial', 30, 'italic')
FONT_WORD = ('돋움', 60, 'bold')

# btn feature
BTN_RELIEF = 'flat'
BTN_BORDER = 1

# 2. change word
words = []


def data_load():
    global words
    data = pd.read_csv('1000_most_common_en_words.csv')
    words = data.to_dict(orient='records')


def change_word():
    idx = rd.randint(0, len(words) - 1)
    card_canvas.itemconfig(word_canvas_lbl, text=words[idx]['en'])


def right():
    change_word()


def wrong():
    change_word()


# 1. ui 만들기
if __name__ == '__main__':
    # window create
    window = Tk()
    window.title(TITLE)
    window.resizable(RESIZABLE, RESIZABLE)
    window.config(bg=BACKGROUND_COLOR, padx=WIN_PAD_X, pady=WIN_PAD_Y)

    # images to photoimages
    back_card_img = PhotoImage(file=BACK_CARD_PATH)
    front_card_img = PhotoImage(file=FRONT_CARD_PATH)
    right_img = PhotoImage(file=RIGHT_IMG_PATH)
    wrong_img = PhotoImage(file=WRONG_IMG_PATH)
    # canvas
    card_canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_canvas.create_image(CARD_WIDTH / 2, CARD_HEIGHT / 2, image=front_card_img)
    language_canvas_lbl = card_canvas.create_text(POS_EN_X, POS_EN_Y, text="ENGLISH", font=FONT_LANGUAGE)
    word_canvas_lbl = card_canvas.create_text(POS_KO_X, POS_KO_Y, font=FONT_WORD, text="한글" )

    # Button
    right_btn = Button(image=right_img, bd=BTN_BORDER, highlightthickness=0, relief=BTN_RELIEF, command=right)
    wrong_btn = Button(image=wrong_img, bd=BTN_BORDER, highlightthickness=0, relief=BTN_RELIEF, command=wrong)

    # positioning
    card_canvas.grid(row=1, column=1, columnspan=2)
    wrong_btn.grid(row=2, column=1)
    right_btn.grid(row=2, column=2)

    data_load()
    change_word()

    window.mainloop()
