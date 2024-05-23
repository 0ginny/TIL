from tkinter import *

LOGO_IMAGE_PATH = 'logo.png'

WINDOW_PAD_X = 50
WINDOW_PAD_Y = 50

FONT = ('Arial', 12 , 'normal')
WEB_ENTRY_WIDTH = 36
PW_ENTRY_WIDTH = 21

PW_BTN_WIDTH = 15
ENTER_BTN_WIDTH = 36
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
    pw_ety = Entry(width=PW_ENTRY_WIDTH,font=FONT)

    # Buttons
    pw_btn = Button(text="Generate Password", width=PW_BTN_WIDTH, font=FONT)
    enter_btn = Button(text="Add", width=ENTER_BTN_WIDTH, font=FONT)

    # widget positioning
    logo_canvas.grid(row = 1, column = 2)
    web_lbl.grid(row = 2, column = 1)
    email_lbl.grid(row = 3, column = 1)
    password_lbl.grid(row = 4, column = 1)
    web_ety.grid(row = 2, column = 2, columnspan = 2)
    email_ety.grid(row = 3, column = 2, columnspan = 2)
    pw_ety.grid(row = 4, column = 2)
    pw_btn.grid(row = 4, column = 3)
    enter_btn.grid(row = 5, column = 2, columnspan = 2)

    window.mainloop()
