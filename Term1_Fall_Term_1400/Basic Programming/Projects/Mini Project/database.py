from tkinter import *


master = Tk()
with open('database.txt', 'a+') as data :
    name = input()
    data.write(name)

lb = Label(master, text = 'Hi'+ ' ' + name)
lb.pack() 
master.mainloop()