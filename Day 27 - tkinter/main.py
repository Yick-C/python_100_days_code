from tkinter import *  # can just import tkinter or a few modules

# Button

def button_clicked():
    my_label["text"] = input.get()

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # Add padding

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)  # Place component on screen and centers it

my_label["text"] = "New Text"
my_label.config(text="Another way test")
my_label["text"] = "The Label"

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click Me too", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10, )
input.grid(column=3, row=2)

# Pack, not good if you want specific positioning
# Place, for precise positioning
# Grid
# Cannot mix both Grid and Pack


window.mainloop()