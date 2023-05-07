from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():

    passoword_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = passoword_letters + password_symbols + password_numbers
    shuffle(password_list)
    new_password = "".join(password_list)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = username_entry.get()
    pd = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pd,
        }
    }

    if len(website) == 0 or len(pd) == 0:
        messagebox.showinfo(title="Missing Input", message="please fill in all the details")
    else:
        try:
            with open("Data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("Data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- SEARCH ------------------------------- #


def search():

    website = website_entry.get()
    try:
        with open("Data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Credentials not found", message="Account not found, please check the Website "
                                                                   "name")
    else:
        if website in data:
            email = data[website]["email"]
            password_1 = data[website]["password"]
            messagebox.showinfo(title=f"Credentials of {website}", message=f"Email: {email} \n"
                                                                     f"Password: {password_1}")
        else:
            messagebox.showinfo(title="Credentials not found", message="Account not found, please check the Website "
                                                                       "name")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website :")
website_label.grid(row=1, column=0)
username = Label(text="Email/Username :")
username.grid(row=2, column=0)
password = Label(text="Password :")
password.grid(row=3, column=0)

#Buttons
gen_pass = Button(text="Generate Password", command=password_generator, width=20)
gen_pass.grid(row=3, column=2)
add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=20, command=search)
search_button.grid(row=1, column=2,)

#Entrys
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=30)
username_entry.grid(row=2, column=1)
username_entry.insert(0,"rishibalaji2104@gmail.com")
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

window.mainloop()