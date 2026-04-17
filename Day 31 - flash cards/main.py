from tkinter import *
import random
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 30, "italic")
FONT_WORD = ("Arial", 40, "bold")

data = pandas.read_csv("data/chinese_words_hsk3.csv")
df_list = data.to_dict(orient="records")
current_card = {}
# ---------------------------- READ LANGUAGE FILE ------------------------------- #
def get_next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(df_list)
    canvas.itemconfig(title_text, text="Chinese", fill="black")
    canvas.itemconfig(word_text, text=current_card['Chinese'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(title_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=current_card['English'])
    canvas.itemconfig(pinyin_text, fill="white", text=current_card['Pinyin'])

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
correct_btn_img = PhotoImage(file="images/right.png")
correct_btn = Button(image=correct_btn_img, command=get_next_word)
correct_btn.grid(row=1, column=1)

wrong_btn_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, command=get_next_word)
wrong_btn.grid(row=1, column=0)

get_next_word()

window.mainloop()