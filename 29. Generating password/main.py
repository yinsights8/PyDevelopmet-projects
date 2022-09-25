import json
from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
               'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symb in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, f"{password}")
    pyperclip.copy(password)


# ----------------------------------------------------------- SAVE PASSWORD -------------------------------------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    show_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Opps', message="Please do not leave any empty information.")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                read = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode='w') as data_file:
                json.dump(show_data, data_file, indent=4)
                # data_file.write(f"{website} | {email} | {password} \n")

        else:
            read.update(show_data)
            with open("data.json", 'w') as data_file:
                json.dump(read, data_file, indent=4)

        finally:

            website_input.delete(0, END)
            password_input.delete(0, END)


# ----------------------------------------------------------- FIND PASSWORD -------------------------------------------------------------- #
def find_password():
    website = website_input.get()

    with open("data.json", "r") as data_read:
        read_d = json.load(data_read)

        if website in read_d:
            email = read_d[website]["email"]
            password = read_d[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email : {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="FileNotFound", message=f"data for {website} not exits")


# ----------------------------------------------------------- UI SETUP -------------------------------------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200, width=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=35)
website_input.place(x=100, y=207)
website_input.focus()
email_input = Entry(width=51)
email_input.insert(END, "Example@gamil.com")
email_input.place(x=100, y=231)
password_input = Entry(width=35)
password_input.place(x=100, y=255)

# Buttons

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=3)

genarate_pass_button = Button(text="Generate password", command=generate_pass)
genarate_pass_button.grid(column=2, row=3)

search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(column=2, row=1)
window.mainloop()