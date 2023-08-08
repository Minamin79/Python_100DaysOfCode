from tkinter import *
import pandas
import random

BACKGROUND_COLOR = '#B1DDC6'
current_card = {}
to_learn = {}

try:
    data_file = pandas.read_csv('data/Words_I_Should_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data_file.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(title_txt, fill='black', text='French')
    canvas.itemconfig(word_txt, fill='black', text=current_card['French'])
    flip_timer = window.after(3000, func=flip_card)

def knew_it():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/Words_I_Should_learn.csv', index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(title_txt, fill='white', text='English')
    canvas.itemconfig(word_txt, fill='white', text=current_card['English'])
    

window = Tk()
window.title('FlashCard')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=550)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_txt = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
word_txt = canvas.create_text(400, 300, text='Word', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=3)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=next_card, highlightthickness=0)
wrong_button.grid(row=2, column=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, command=knew_it, highlightthickness=0)
right_button.grid(row=2, column=3)

next_card()


window.mainloop()