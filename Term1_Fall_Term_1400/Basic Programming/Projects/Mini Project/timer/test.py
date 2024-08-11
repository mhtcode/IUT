<<<<<<< HEAD
from tkinter import *
from tkinter import messagebox
import time as ts
# ---------------------------- CONSTANTS ------------------------------- #

time = 3


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
work_sec  = time
SHORT_BREAK_MIN = 0
LONG_BREAK_MIN = 0
reps = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'{time}')
    title_label.config(text="Timer")
    
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1 
    count_down(work_sec)
    title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    
    count_sec = count 

    canvas.itemconfig(timer_text, text=f"{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        messagebox.showinfo("Time countdown", "Time's Up = > You lose")
        ts.sleep(1)
        quit()
    
    
        

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.geometry('500x400')
window.title("Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# label
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
title_label.place(x = 200, y=63)

# config UI for canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # add background, remove border
tomato_img = PhotoImage(file="timer01.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"{time}", fill="blue", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# buttons

start_button = Button(text="Start", highlightthickness=0, bg="#F1583F", fg="#fff", font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.place(x = 0, y=250)


reset_button = Button(text="Reset", highlightthickness=0, bg="#F1583F", fg="#fff", font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.place(x = 150, y=250)

exit_button = Button(  bg="#F1583F", fg="#fff", text = "Exit", command = quit)
exit_button.place(x = 100, y=255)

pause_button = Button(text="Pause", fg="#fff", bg="#F1583F")
pause_button.place(x = 95, y=215)









window.mainloop()
=======
from tkinter import *
from tkinter import messagebox
import time as ts
# ---------------------------- CONSTANTS ------------------------------- #

time = 3


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
work_sec  = time
SHORT_BREAK_MIN = 0
LONG_BREAK_MIN = 0
reps = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'{time}')
    title_label.config(text="Timer")
    
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1 
    count_down(work_sec)
    title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    
    count_sec = count 

    canvas.itemconfig(timer_text, text=f"{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        messagebox.showinfo("Time countdown", "Time's Up = > You lose")
        ts.sleep(1)
        quit()
    
    
        

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.geometry('500x400')
window.title("Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# label
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
title_label.place(x = 200, y=63)

# config UI for canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # add background, remove border
tomato_img = PhotoImage(file="timer01.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"{time}", fill="blue", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# buttons

start_button = Button(text="Start", highlightthickness=0, bg="#F1583F", fg="#fff", font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.place(x = 0, y=250)


reset_button = Button(text="Reset", highlightthickness=0, bg="#F1583F", fg="#fff", font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.place(x = 150, y=250)

exit_button = Button(  bg="#F1583F", fg="#fff", text = "Exit", command = quit)
exit_button.place(x = 100, y=255)

pause_button = Button(text="Pause", fg="#fff", bg="#F1583F")
pause_button.place(x = 95, y=215)









window.mainloop()
>>>>>>> deba06a (BP Projects Added)
