<<<<<<< HEAD
import time
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
timer = None


# Style :
root = Tk()
root.geometry('600x550')
bg = PhotoImage(file="timer.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

ico = Image.open('timer.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


root.title("Counter")


minute = StringVar()
second = StringVar()


def reset_timer():
    root.after_cancel(timer)
    # canvas.itemconfig(timer_text, text=str(WORK_MIN))
    # title_label.config(text="Timer")

    global reps
    reps = 0


def submit():
    try:
        temp = int(second=10)
    except:
        print("Please input the right value")
    while temp > -1:

        root.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("Time countdown", "Time's Up")
        temp -= 1


# label
title_label = Label(root, text="Timer", fg='green',
                    font=(FONT_NAME, 35, "bold"))
title_label.grid(column=4, row=2)

# # config UI for canvas
# canvas = Canvas(width=200, height=224,  highlightthickness=0)  # add background, remove border

# timer_text = canvas.create_text(100, 130, text=f"{WORK_MIN}", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=2, row=1)


# # Add buttons
button1 = Button(root, bg="#F1583F", fg="#fff", text="Exit", command=quit)
button1.place(x=100, y=465)

button2 = Button(root, bg="#F1583F", fg="#fff", text="Start", command=submit)
button2.place(x=270, y=465)

button3 = Button(root, bg="#F1583F", fg="#fff",
                 text="Reset", command=reset_timer)
button3.place(x=440, y=465)


root.mainloop()
=======
import time
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
timer = None


# Style :
root = Tk()
root.geometry('600x550')
bg = PhotoImage(file="timer.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

ico = Image.open('timer.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


root.title("Counter")


minute = StringVar()
second = StringVar()


def reset_timer():
    root.after_cancel(timer)
    # canvas.itemconfig(timer_text, text=str(WORK_MIN))
    # title_label.config(text="Timer")

    global reps
    reps = 0


def submit():
    try:
        temp = int(second=10)
    except:
        print("Please input the right value")
    while temp > -1:

        root.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("Time countdown", "Time's Up")
        temp -= 1


# label
title_label = Label(root, text="Timer", fg='green',
                    font=(FONT_NAME, 35, "bold"))
title_label.grid(column=4, row=2)

# # config UI for canvas
# canvas = Canvas(width=200, height=224,  highlightthickness=0)  # add background, remove border

# timer_text = canvas.create_text(100, 130, text=f"{WORK_MIN}", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=2, row=1)


# # Add buttons
button1 = Button(root, bg="#F1583F", fg="#fff", text="Exit", command=quit)
button1.place(x=100, y=465)

button2 = Button(root, bg="#F1583F", fg="#fff", text="Start", command=submit)
button2.place(x=270, y=465)

button3 = Button(root, bg="#F1583F", fg="#fff",
                 text="Reset", command=reset_timer)
button3.place(x=440, y=465)


root.mainloop()
>>>>>>> deba06a (BP Projects Added)
