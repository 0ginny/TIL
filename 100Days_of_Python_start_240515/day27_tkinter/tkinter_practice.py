import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tk.Label(text = 'I am a Label')
my_label.pack() # 이게 있어야 window 안에 넣을 수 있어

def button_clicked():
    text = input_text.get()
    my_label['text'] = f"{text} clicked"
    # my_label.config(text='clicked')


button = tk.Button(text="click", command=button_clicked)
button.pack()

input_text = tk.Entry(width= 10)
input_text.pack()


window.mainloop()
