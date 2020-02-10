from tkinter import *
windows = Tk()
windows.title("my first program")
windows.geometry("720x360+430+260")

text1 = Label(windows, text="my first text", font=("arial", 20) )
text1.grid()
text2 = Label(windows, text="Ready, Set, Go!", font=("aria", 10) )
text2.grid()
text3 = Label(windows, text="Арсений ГОБЛИН!!!",font=("aria", 50) )
text3.grid()

windows.mainloop()
