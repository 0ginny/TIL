from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
STRAT_ON = False

# ---------------------------- TIMER RESET ------------------------------- #
def Timer_Reset():
    global reps, STRAT_ON
    window.after_cancel(timer)
    timer_text.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_time, text="00:00")
    check_text.config(text="")
    reps = 0
    STRAT_ON = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def Timer_Start():
    global STRAT_ON
    if not STRAT_ON:
        STRAT_ON = True
        Timer_ON()

def Timer_ON():
    global reps
    reps += 1
    mark = ''
    # 1,3,5,7 Work
    if reps % 2:
        if reps % 8 == 1:
            check_text.config(text='')
        count_down(WORK_MIN * 60)
        timer_text.config(text='Work', fg=GREEN)

    else:  # 2,4,6,8 Break
        check_repeat = (reps // 2) % 4
        for _ in range(check_repeat):
            mark += CHECK_MARK

        if reps % 8 == 0:  # Long Break
            mark = CHECK_MARK * 4
            count_down(LONG_BREAK_MIN * 60)
            timer_text.config(text='Break', fg=RED)
        else:
            count_down(SHORT_BREAK_MIN * 60)
            timer_text.config(text='Break', fg=PINK)
        check_text.config(text=mark)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer

    count_min = count // 60
    count_second = count % 60
    # second 두자리로 만들기
    if count_second < 10:
        count_second = f'0{count_second}'

    canvas.itemconfig(timer_time, text=f'{count_min}:{count_second}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        Timer_ON()


# ---------------------------- UI SETUP ------------------------------- #

if __name__ == '__main__':
    # create window
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    # tomato canvas
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file='tomato.png')
    canvas.create_image(100, 112, image=tomato_img)
    timer_time = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))

    # Text
    timer_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, 'bold'), bg=YELLOW)
    check_text = Label(fg=GREEN, font=(FONT_NAME, 12, 'normal'), bg=YELLOW)

    # buttons
    start_btn = Button(text="Start", font=(FONT_NAME, 12, 'normal'), highlightthickness=0, command=Timer_Start)
    reset_btn = Button(text="Reset", font=(FONT_NAME, 12, 'normal'), highlightthickness=0, command=Timer_Reset)

    # widget placing
    timer_text.grid(row=1, column=2)
    canvas.grid(row=2, column=2)
    start_btn.grid(row=3, column=1)
    reset_btn.grid(row=3, column=3)
    check_text.grid(row=4, column=2)

    window.mainloop()

'''
dynamic typing

변수를 바꿨을 때 자동적으로 변수의 타입도 바꿔주는 것.

'''
