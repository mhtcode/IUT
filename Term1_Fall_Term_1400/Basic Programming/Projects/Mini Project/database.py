<<<<<<< HEAD
from tkinter import *


master = Tk()
with open('database.txt', 'a+') as data :
    name = input()
    data.write(name)

lb = Label(master, text = 'Hi'+ ' ' + name)
lb.pack() 
=======
from tkinter import *


master = Tk()
with open('database.txt', 'a+') as data :
    name = input()
    data.write(name)

lb = Label(master, text = 'Hi'+ ' ' + name)
lb.pack() 
>>>>>>> deba06a (BP Projects Added)
master.mainloop()