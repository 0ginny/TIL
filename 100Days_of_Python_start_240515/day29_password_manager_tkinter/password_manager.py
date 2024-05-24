from tkinter import *
from tkinter import messagebox  # 이건 클래스가 아니라 module 이라 * 해도 따로 import 해야해.
import random as rd
import pyperclip
import json

LOGO_IMAGE_PATH = 'logo.png'

WINDOW_PAD_X = 50
WINDOW_PAD_Y = 50

FONT = ('Arial', 12, 'normal')
WEB_ENTRY_WIDTH = 36
PW_ENTRY_WIDTH = 21

PW_BTN_WIDTH = 15
ENTER_BTN_WIDTH = 36

SAVE_TXT_PATH = 'data.txt'
SAVE_JSON_PATH = 'pw_data.json'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pw():
    pw_ety.delete(0, END)

    letters_list = [rd.choice(letters) for _ in range(rd.randint(8, 10))]
    nums_list = [rd.choice(numbers) for _ in range(rd.randint(2, 4))]
    symbols_list = [rd.choice(symbols) for _ in range(rd.randint(2, 4))]

    password_list = letters_list + nums_list + symbols_list
    rd.shuffle(password_list)
    gen_pw = ''.join(password_list)

    pw_ety.insert(0, gen_pw)
    pyperclip.copy(gen_pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_txt():
    web = web_ety.get()
    email = email_ety.get()
    pw = pw_ety.get()

    new_data = {web: {
        "email": email,
        "password": pw
    }}

    if len(web) * len(pw):
        save_ok = messagebox.askokcancel(title=web,
                                         message=f'These are the details entered:\nEmail : {email}\nPassword : {pw}\nIs it ok to save?')
        if save_ok:
            try:
                with open(SAVE_JSON_PATH, mode='r') as data_file:
                    # json load
                    data = json.load(data_file
            except:
                with open(SAVE_JSON_PATH, mode='w') as data_file:
                    json.dump(obj=new_data, fp=data_file, indent=4)
            else:
                # json data update to dict
                data.update(new_data)
                with open(SAVE_JSON_PATH, mode='w') as data_file:
                    # save data to json file
                    json.dump(obj=data, fp=data_file, indent=4)
            finally :
                web_ety.delete(0,END)
                pw_ety.delete(0,END)
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")


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
    pw_btn = Button(text="Generate Password", width=PW_BTN_WIDTH, font=FONT, command=generate_pw)
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
