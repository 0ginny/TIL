import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text = 'I am a Label')
my_label.pack() # 이게 있어야 window 안에 넣을 수 있어

window.mainloop()
