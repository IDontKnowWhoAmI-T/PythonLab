from tkinter import *
windows = Tk()
windows.title("my second program")
windows.geometry("1000x1000+430+260")

t = Label(windows, text="Телепрограмма", fg="#494ede", font=("arial", 15))
t.grid()
d = Label(windows, text="17:35",  font=("arial", 10))
d.grid(column=0,row=1)
r = Label(windows, text="Роман в камне", font=("arial", 10))
r.grid(column=1,row=1)
k = Label(windows, text="Культура",fg="#706d6d", font=("arial", 10))
k.grid(column=2,row=1)


windows.mainloop
