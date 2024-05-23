from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
def Timer_Reset():
    pass


def Timer_Start():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

if __name__ == '__main__':
    # create window
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=100, bg=YELLOW)

    # tomato canvas
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file='tomato.png')
    canvas.create_image(100, 112, image=tomato_img)
    canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))

    # Text
    timer_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, 'bold'), bg=YELLOW)
    check_text = Label(text="✔", fg=GREEN, font=(FONT_NAME, 12, 'normal'), bg=YELLOW)

    # buttons
    start_btn = Button(text="Start", font=(FONT_NAME, 12, 'normal'), highlightthickness=0)
    reset_btn = Button(text="Reset", font=(FONT_NAME, 12, 'normal'), highlightthickness=0)

    # widget placing
    timer_text.grid(row=1, column=2)
    canvas.grid(row=2, column=2)
    start_btn.grid(row=3, column=1)
    reset_btn.grid(row=3, column=3)
    check_text.grid(row=4, column=2)

    window.mainloop()
