from tkinter import *

text = """
17:35 Чужой район-3 Пятый канал
17:35 Вести Россия 24
17:40 Папик СТС
"""

windows = Tk()
windows.title("program")
windows.geometry("800x250+430+260")

m = Label(windows, text="Эфир", font=("arial", 20))
m.grid(row=0, column=0)

r = Button(windows, text="Рекомендации", font=("arial", 10), width=15, height=1, fg="#ffffff", bg="#000000")
r.grid(row=1, column=0)

f= Button(windows, text="Фильмы", font=("arial", 10), width=15, height=1, fg="#000000", bg="#d7ddfc")
f.grid(row=1, column=1)

s= Button(windows, text="Сериалы", font=("arial", 10), width=15, height=1, fg="#000000", bg="#d7ddfc")
s.grid(row=1, column=2)

sp= Button(windows, text="Спорт", font=("arial", 10), width=15, height=1, fg="#000000", bg="#d7ddfc")
sp.grid(row=1, column=3)

b= Button(windows, text="Блогеры", font=("arial", 10), width=15, height=1, fg="#000000", bg="#d7ddfc")
b.grid(row=1, column=4)

k= Button(windows, text="Киберспорт", font=("arial", 10), width=15, height=1, fg="#000000", bg="#d7ddfc")
k.grid(row=1, column=5)

t = Label(windows, text=text, font=("arial", 15))
t.grid(row=2, column=1, columnspan = 4)






windows.mainloop()
