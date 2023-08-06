from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    screen.after_cancel(timer)
    reps = 1
    timer_label.config(text="Timer", foreground=GREEN)
    canvas.itemconfig(timer_canvas, text="00:00")
    tick_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    count_down(25*60)
    timer_label.config(text="Work", font=(FONT_NAME, 33, "bold"), foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_canvas, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = screen.after(1000, count_down, count - 1)
    else:
        reps += 1
        if reps % 2 == 0:
            tick_label.config(text="✔" * round(reps / 2))
        if reps == 9:
            timer_label.config(text="Well done!", foreground=RED)
            screen.after_cancel(timer)
        elif reps % 2 == 1:
            count_down(WORK_MIN*60)
            timer_label.config(text="Work", foreground=GREEN)
        elif reps == 8:
            count_down(LONG_BREAK_MIN*60)
            timer_label.config(text="Long rest", foreground=RED)
        else:
            timer_label.config(text="Short rest", foreground=PINK)
            count_down(SHORT_BREAK_MIN*60)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Pomodoro")
screen.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_canvas = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 33, "bold"), foreground=GREEN)
timer_label.grid(column=1, row=0)
tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start)
start_button.grid(column=0, row=3)
reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=3)
screen.mainloop()
