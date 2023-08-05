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
REPS = 0
CHECK_MARKS = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text='00:00')
    timer_label.config(text='Timer')
    mark_label.config(text='')
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    if REPS % 2 == 0:
        if REPS == 8:
            count_down(LONG_BREAK_MIN * 60)
            timer_label.config(text='Break', fg=RED)
        else:
            count_down(SHORT_BREAK_MIN * 60)
            timer_label.config(text='Break', fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_txt, text=f'{math.floor(count / 60)}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(REPS / 2)
        for i in range(work_sessions):
            marks += '✅'
        mark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=90, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(column=2, row=1)

mark_label = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10))
mark_label.grid(column=2, row=4)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=3, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=photo)
timer_txt = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25,'bold'))
canvas.grid(column=2, row=2)


window.mainloop()