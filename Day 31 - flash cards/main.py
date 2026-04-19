from tkinter import *
import random
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 30, "italic")
FONT_WORD = ("Arial", 40, "bold")
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/chinese_words_hsk3.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- READ LANGUAGE FILE ------------------------------- #
def get_next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="Chinese", fill="black")
    canvas.itemconfig(word_text, text=current_card['Chinese'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(title_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=current_card['English'])
    canvas.itemconfig(pinyin_text, fill="white", text=current_card['Pinyin'])

def is_known():
    to_learn.remove(current_card)
    learn_list = pandas.DataFrame(to_learn)
    learn_list.to_csv("data/words_to_learn.csv", index=False)  # Don't add index to csv
    get_next_word()

# ---------------------------- FLASH CARD UI ------------------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", font=FONT_TITLE)
word_text = canvas.create_text(400, 260, text="", font=FONT_WORD)
pinyin_text = canvas.create_text(400, 360, text="", font=FONT_TITLE)
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
known_btn_img = PhotoImage(file="images/right.png")
known_btn = Button(image=known_btn_img, command=is_known)
known_btn.grid(row=1, column=1)

unknown_btn_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=unknown_btn_img, command=get_next_word)
unknown_btn.grid(row=1, column=0)

get_next_word()

window.mainloop()