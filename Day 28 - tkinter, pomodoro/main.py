from tkinter import *
import math
# Event Driven - Pomodoro project
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    start_btn["state"] = "active"
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    start_btn["state"] = "disabled"

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Pushes window to the front when the countdown is over
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)
    window.bell()  # alert sound

    if reps % 8 == 0:  # if its 8th rep
        countdown(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:  # if its 2nd/4th/6th
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:  # if it's 1st/3rd/5th/7th
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)  # 1 sec is 1000ms, function, positional parameters
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)  # Every 2 reps is a completed session
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Grid - 4 rows, 3 columns
# Title
title_label = Label(text="Timer", font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW, width=11)
title_label.grid(row=0, column=1)

# Canvas image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # fg to colour foreground
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 134, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start_btn = Button(text="Start", command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(row=2, column=2)

# Checkmark
checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)


window.mainloop()
