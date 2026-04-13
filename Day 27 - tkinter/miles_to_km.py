from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)  # Add padding


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    number_of_km.config(text=f"{km}")


# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label
is_equal_text = Label(text="is equal to")
is_equal_text.grid(column=0, row=1)

# Label
number_of_km = Label(text="0")
number_of_km.grid(column=1, row=1)

# Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=3)


window.mainloop()