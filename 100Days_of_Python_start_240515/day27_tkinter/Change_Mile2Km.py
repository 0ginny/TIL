from tkinter import *

FONT = ('Arial', 12, 'bold')
WIDTH = 300
HEIGHT = 100

PADDING_X = 20
PADDING_Y = 20

GRID_PAD_LEFT = 5
GRID_PAD_RIGHT = 5
GRID_PAD_TOP = 5
GRID_PAD_BOTTOM = 5

MILE_ENTRY_WIDTH = 5

ALIGN = 'center'

CVT_VAL = 0


# Convert mile to km
def CVT_Mile2Km():
    mile = int(mile_input.get())
    km = 1.609 * mile
    km_value_txt['text'] = str(km)


# create window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=PADDING_X, pady=PADDING_Y)

# label 생성
mile_txt = Label(text='Mile', font=FONT)
km_txt = Label(text=" Km", font=FONT)
equal_txt = Label(text='is equal to', font=FONT)
km_value_txt = Label(text=f'{CVT_VAL}', font=FONT)

# TXT 박스 생성
mile_input = Entry(justify=ALIGN, font=FONT)
mile_input.config(width=MILE_ENTRY_WIDTH)

# Button 생성
cal_btn = Button(text="Calculate", font=FONT, command=CVT_Mile2Km)

# 위치 지정
mile_input.grid(column=2, row=1, padx=(GRID_PAD_LEFT, GRID_PAD_RIGHT), pady=(GRID_PAD_TOP, GRID_PAD_BOTTOM))
mile_txt.grid(column=3, row=1, padx=(GRID_PAD_LEFT, GRID_PAD_RIGHT), pady=(GRID_PAD_TOP, GRID_PAD_BOTTOM))
equal_txt.grid(column=1, row=2, padx=(GRID_PAD_LEFT, GRID_PAD_RIGHT), pady=(GRID_PAD_TOP, GRID_PAD_BOTTOM))
km_value_txt.grid(column=2, row=2, padx=(GRID_PAD_LEFT, GRID_PAD_RIGHT), pady=(GRID_PAD_TOP, GRID_PAD_BOTTOM))
km_txt.grid(column=3, row=2, padx=(GRID_PAD_LEFT, GRID_PAD_RIGHT), pady=(GRID_PAD_TOP, GRID_PAD_BOTTOM))
cal_btn.grid(column=2, row=3, padx=(GRID_PAD_LEFT, GRID_PAD_RIGHT), pady=(GRID_PAD_TOP, GRID_PAD_BOTTOM))

window.mainloop()
