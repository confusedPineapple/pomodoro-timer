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
reps = 8
checks = ['✔','✔✔','✔✔✔','✔✔✔✔']
num = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'00:00')
    my_label.config(text='Timer')
    Check_mark.config(text='')
    global reps
    global num
    num = 0
    reps = 8

def complete():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'00:00')
    my_label.config(text='Pomodoro Session Complete')
    Check_mark.config(text='')
    global reps
    global num
    num = 0
    reps = 8


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global num
    if reps % 2 == 0:
        count_down(WORK_MIN * 60)
        my_label.config(text='Work',fg=GREEN)

    elif reps == 1:
        count_down(LONG_BREAK_MIN * 60)
        my_label.config(text='Long Break',fg=RED)
        Check_mark.config(text=checks[num])
        num += 1
    else:
        count_down(SHORT_BREAK_MIN * 60)
        my_label.config(text='Short Break',fg=PINK)
        Check_mark.config(text=checks[num])
        num += 1

    reps -= 1
    if reps < 0:
        complete()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=50, pady=50, bg=YELLOW)


my_label = Label(text="Timer",  fg=GREEN,  bg=YELLOW,font=(FONT_NAME, 24,'bold'))
my_label.grid(column=1,row=0)


canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0 )
img  = PhotoImage(file='tomato.png')
canvas.create_image(100, 100, image = img)
timer_text = canvas.create_text(103,130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1,row=1)


button1 = Button(text='Start', command=start_timer)
button1.grid(column=0,row=2)
button2 = Button(text='Reset', command=reset_timer)
button2.grid(column=2,row=2)


Check_mark = Label(fg=GREEN,bg=YELLOW)
Check_mark.grid(column=1,row=2)
window.mainloop()