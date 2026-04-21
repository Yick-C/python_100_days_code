from tkinter import *
import requests

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    response.raise_for_status()
    quote = response.json()[0]['q']
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("They Say...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Quote Goes HERE", width=250, font=("Arial", 18, "bold"), fill="white")
canvas.grid(row=0, column=0)

thinking_img = PhotoImage(file="thinking.png")
thinking_button = Button(image=thinking_img, highlightthickness=0, command=get_quote)
thinking_button.grid(row=1, column=0)

get_quote()

window.mainloop()