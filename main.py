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
rep_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    if rep_timer:
        window.after_cancel(rep_timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", fg="black")   # Default black
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break", fg="blue")  # Blue for long break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break", fg=PINK)   # Pink for short break
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=RED)           # Red for work
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")

    if count > 0:
        global rep_timer
        rep_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = "✔" * (reps // 2)
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

timer = Label(text="Timer", fg=RED, bg=GREEN, font=(FONT_NAME, 50))
timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check_marks = Label(text="", fg=YELLOW, bg=GREEN, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)

window.mainloop()
