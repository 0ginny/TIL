from tkinter import *
from tkinter import messagebox  # 이건 클래스가 아니라 module 이라 * 해도 따로 import 해야해.

LOGO_IMAGE_PATH = 'logo.png'

WINDOW_PAD_X = 50
WINDOW_PAD_Y = 50

FONT = ('Arial', 12, 'normal')
WEB_ENTRY_WIDTH = 36
PW_ENTRY_WIDTH = 21

PW_BTN_WIDTH = 15
ENTER_BTN_WIDTH = 36

SAVE_FILE_PATH = 'data.txt'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_txt():
    web = web_ety.get()
    email = email_ety.get()
    pw = pw_ety.get()

    save_ok = messagebox.askokcancel(title=web,
                                     message=f'These are the details entered:\nEmail : {email}\nPassword : {pw}\nIs it ok to save?')

    if save_ok:
        with open(SAVE_FILE_PATH, mode='a') as file:
            file.write(f'{web} | {email} | {pw}\n')
            web_ety.delete(0, END)
            pw_ety.delete(0, END)
            web_ety.focus()


# ---------------------------- UI SETUP ------------------------------- #

if __name__ == "__main__":
    # create window
    window = Tk()
    window.config(padx=WINDOW_PAD_X, pady=WINDOW_PAD_Y)

    # logo canvas
    logo_image = PhotoImage(file=LOGO_IMAGE_PATH)
    logo_canvas = Canvas(width=200, height=200)
    logo_canvas.create_image(100, 100, image=logo_image)

    # Labels
    web_lbl = Label(text="Website:", font=FONT)
    email_lbl = Label(text="Email/Username:", font=FONT)
    password_lbl = Label(text="Password:", font=FONT)

    # Entries
    web_ety = Entry(width=WEB_ENTRY_WIDTH, font=FONT)
    email_ety = Entry(width=WEB_ENTRY_WIDTH, font=FONT)
    email_ety.insert(0, "kginny@gmail.com")
    pw_ety = Entry(width=PW_ENTRY_WIDTH, font=FONT)

    # Buttons
    pw_btn = Button(text="Generate Password", width=PW_BTN_WIDTH, font=FONT)
    enter_btn = Button(text="Add", width=ENTER_BTN_WIDTH, font=FONT, command=save_to_txt)

    # widget positioning
    logo_canvas.grid(row=1, column=2)
    web_lbl.grid(row=2, column=1)
    email_lbl.grid(row=3, column=1)
    password_lbl.grid(row=4, column=1)
    web_ety.grid(row=2, column=2, columnspan=2)
    web_ety.focus()  # 커서 옮기기
    email_ety.grid(row=3, column=2, columnspan=2)
    pw_ety.grid(row=4, column=2)
    pw_btn.grid(row=4, column=3)
    enter_btn.grid(row=5, column=2, columnspan=2)

    window.mainloop()
