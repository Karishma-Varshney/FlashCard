from tkinter import *
import pandas
import random

data = pandas.read_csv('french_words.csv')
to_learn = data.to_dict(orient='records')
current_word = {}


def change():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(flash_title, text='French', fill='black')
    canvas.itemconfig(flash_word, text=current_word['French'], fill='black')
    canvas.itemconfig(flash_img, image=front_img)
    flip_timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(flash_title, text='English', fill='white')
    canvas.itemconfig(flash_word, text=current_word['English'], fill='white')
    canvas.itemconfig(flash_img, image=back_img)


# ----------------------------UI SETUP------------------------#
BACKGROUND_COLOR = "#FFFFDD"

window = Tk()
window.title('My Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=520, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='card_front.png')
back_img = PhotoImage(file='card_back.png')
flash_img = canvas.create_image(400, 260, image=front_img)
flash_title = canvas.create_text(400, 140, text='Title', font='Arial 40 italic')
flash_word = canvas.create_text(400, 260, text='word', font='Arial 60 bold')
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file='wrong.png')
cross_button = Button(image=cross_img, command=change)
cross_button.grid(row=1, column=0)

check_img = PhotoImage(file='right.png')
check_button = Button(image=check_img, command=change)
check_button.grid(row=1, column=1)

change()

window.mainloop()
