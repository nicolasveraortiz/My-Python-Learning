from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    password = password_entry.get()
    web = web_entry.get()
    user = user_entry.get()
    new_data = {web: {
        "user": user,
        "password": password
    }}
    if password == "" or web == "" or user == "":
        messagebox.showerror(title="Error", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"These are the details entered: \nEmail: {web}"
                                                                     f"\nPassword: {password}\nAre these ok?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Not Data File Found")
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title="Error", message="No info in data file")
    else:
        web = web_entry.get()
        if web in data:
            messagebox.showinfo(title="Account Data",
                                message=f"In {web}, your user and password are:\nUsername: {data[web]['user']}"
                                        f"\nPassword: {data[web]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for '{web}' exists.")


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("My Password Generator")
screen.config(padx=50, pady=50)

image_canvas = Canvas(width=200, height=189, highlightthickness=1)
logo = PhotoImage(file="logo.png")
image_canvas.create_image(100, 95, image=logo)
image_canvas.grid(column=1, row=1)

web_label = Label(text="Website: ")
web_label.grid(column=0, row=2)
user_label = Label(text="Email/Username: ")
user_label.grid(column=0, row=3)
password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

web_entry = Entry(width=45)
web_entry.grid(column=1, row=2, columnspan=2)
web_entry.focus()
user_entry = Entry(width=45)
user_entry.grid(column=1, row=3, columnspan=2)
user_entry.insert(0, "clivionicolasveraortiz1@gmail.com")
password_entry = Entry(width=45)
password_entry.grid(column=1, row=4)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=4)
add_button = Button(text="Add", command=add, width=36)
add_button.grid(column=1, row=5, columnspan=2)
search_button = Button(text="Search", command=search, width=14)
search_button.grid(columnspan=2, column=3, row=2)

screen.mainloop()
