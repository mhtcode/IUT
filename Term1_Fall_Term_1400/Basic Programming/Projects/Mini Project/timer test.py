from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #

t = 5*81


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = t
SHORT_BREAK_MIN = 0
LONG_BREAK_MIN = 0
reps = 0
timer = None









# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'{t}')
    title_label.config(text="Timer")
    
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    count_down(t)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(t):
    while t> 0 :
        time.sleep(1)
        t-=1
        canvas.itemconfig(timer_text, text=f"{t}")


    if t > 0:
        global timer
        timer = window.after(1000, count_down, t - 1)
    else:
        start_timer()

    
    
        

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# label
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)

# config UI for canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # add background, remove border
tomato_img = PhotoImage(file="timer01.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"{t}", fill="blue", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# buttons
# start button
start_button = Button(text="Start", highlightthickness=0, bg="#F1583F", fg="#fff", font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(column="0", row=2)

# reset button
reset_button = Button(text="Reset", highlightthickness=0, bg="#F1583F", fg="#fff", font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.grid(column="2", row=2)

button1 = Button(  bg="#F1583F", highlightthickness=0, fg="#fff", text = "Exit", command = quit)
button1.grid(column="1", row=3)

window.mainloop()