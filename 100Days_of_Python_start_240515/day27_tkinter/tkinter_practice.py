import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = tk.Label(text = 'I am a Label')
my_label.grid(row = 0, column = 0) # 이게 있어야 window 안에 넣을 수 있어
# padding
my_label.config(padx= 10, pady = 10)


def button_clicked():
    text = input_text.get()
    my_label['text'] = f"{text} clicked"
    # my_label.config(text='clicked')


button = tk.Button(text="click", command=button_clicked)
button.grid(row = 0, column = 5)

input_text = tk.Entry(width= 10)
input_text.grid(row = 1, column = 1)


window.mainloop()


'''
wedget 위치시키는 방법
1. pack : 채워넣기
2. place : 좌표로 위치시키기
3. grid : 임의의 그리드의 행렬로 위치하기
'''