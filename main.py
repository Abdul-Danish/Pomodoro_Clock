from tkinter import *
import math
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
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(tick_mark, text="")
    canvas.itemconfig(current_status, text="Timer", fill=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    print(reps)
    work_time_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps < 9:
        if reps == 8:
            canvas.itemconfig(current_status, text="Long Break", fill=RED)
            count_down(long_break_sec)
        elif reps % 2 != 0:   # work on 1, 3, 5, 7
            canvas.itemconfig(current_status, text="Work", fill=GREEN)
            count_down(work_time_sec)
        else:   # break on 2, 4, 6
            canvas.itemconfig(current_status, text="Break", fill=PINK)
            count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60          # ???
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            canvas.itemconfig(tick_mark, text="✔")

# ---------------------------- UI SETUP ------------------------------- #

# highlightthickness=0 (remove border)
window = Tk()
window.config(bg=YELLOW)

canvas = Canvas(width=500, height=350, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(250, 175, image=tomato_img)

# Text
timer_text = canvas.create_text(250, 200, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
current_status = canvas.create_text(260, 40, text="Timer", fill=GREEN, font=(FONT_NAME, 34, "bold"))
tick_mark = canvas.create_text(230, 320, fill=GREEN, font=(FONT_NAME, 18, "bold"))

# Button
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text='Reset', command=reset_timer)

start_button.grid(row=2, column=1)
reset_button.grid(row=2, column=3)

canvas.grid(row=2, column=2)


window.mainloop()

