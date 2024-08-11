<<<<<<< HEAD
import time
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry = ('700x250')

ico = Image.open('timer.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


root.title("Counter")


minute = StringVar()
second = StringVar()


minute.set("00")
second.set("00")

'''Build elements'''



minuteEntry = Entry(root, width=3, textvariable = minute,
                    font = ("Arial", 18, ""))
minuteEntry.place(x=20,y=30)
secondEntry = Entry(root, width=3, textvariable = second,
                    font = ("Arial", 18, ""))
secondEntry.place(x=135,y=30)






'''Build fxn'''

def submit():
    try:
        temp =  int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        mins,secs = divmod(temp,60)
        
        
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)
        
        if (temp == 0):
            messagebox.showinfo("Time countdown", "Time's Up")
        temp -=1

button = Button(root, text = "Set Timer Countdown", bd = '5', command = submit)
button.place(x = 35, y=120)


'''Labels'''

m = Label (root, text = "Minute",font = ("Arial", 10, ""))
m.place(x = 20, y=5)

s = Label (root, text = "Seconds",font = ("Arial", 10, ""))
s.place(x = 130, y=5)

root.mainloop()
=======
import time
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry = ('700x250')

ico = Image.open('timer.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


root.title("Counter")


minute = StringVar()
second = StringVar()


minute.set("00")
second.set("00")

'''Build elements'''



minuteEntry = Entry(root, width=3, textvariable = minute,
                    font = ("Arial", 18, ""))
minuteEntry.place(x=20,y=30)
secondEntry = Entry(root, width=3, textvariable = second,
                    font = ("Arial", 18, ""))
secondEntry.place(x=135,y=30)






'''Build fxn'''

def submit():
    try:
        temp =  int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        mins,secs = divmod(temp,60)
        
        
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)
        
        if (temp == 0):
            messagebox.showinfo("Time countdown", "Time's Up")
        temp -=1

button = Button(root, text = "Set Timer Countdown", bd = '5', command = submit)
button.place(x = 35, y=120)


'''Labels'''

m = Label (root, text = "Minute",font = ("Arial", 10, ""))
m.place(x = 20, y=5)

s = Label (root, text = "Seconds",font = ("Arial", 10, ""))
s.place(x = 130, y=5)

root.mainloop()
>>>>>>> deba06a (BP Projects Added)
