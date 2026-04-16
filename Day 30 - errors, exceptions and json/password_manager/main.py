from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)  # Copy password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        is_empty = messagebox.showinfo(title="Warning", message="There's an empty field!")
    else:
        try:
            with open("data.json", 'r') as file:
                # Reading old date
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)  # indent will format it so it's easier to read
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", 'w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)  # indent will format it so it's easier to read
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().strip()
    try:  # Only put the file handling here, other code goes in else statement
        with open("data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:  # No better way to catch file exceptions
        messagebox.showerror(title="Error", message="No data file found.")
    else: # Exceptions should happen rarely so use if/else if possible
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for this website exist.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

## Sticky EW (East West)

# Canvas
canvas = Canvas(height=200, width=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
website_entry.focus()

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
email_entry.insert(0, "example@hotmail.co.uk")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky=EW)

# Buttons
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2, sticky=EW)

add_password_btn = Button(text="Add", width=36, command=save_password)
add_password_btn.grid(row=4, column=1, columnspan=2, sticky=EW)

search_btn = Button(text="Search", command=find_password)
search_btn.grid(row=1, column=2, columnspan=2, sticky=EW)

window.mainloop()