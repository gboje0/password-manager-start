from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for item in range(nr_letters)]
    symbols_list = [random.choice(symbols) for item in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for item in range(nr_numbers)]
    password_list = letter_list + symbols_list + numbers_list

    random.shuffle(password_list)
    password = ""
    for char in password_list:
      password += char

    print(f"Your password is: {password}")
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(username) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="error", message="one or more fields are empty")
    else:
        try:
            with open("myfile.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("myfile.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("myfile.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)
        # is_okay = messagebox.askokcancel(title=website, message=f"Details to save:\nEmail: {username}\nPassword: "
        #                                               f"{password}\n is it okay to save")
        # if is_okay:
        #     with open("myfile.txt", "a") as data_file:
        #         data_file.write(f"{username}| {website} | {password}\n")
        #         website_input.delete(0, END)
        #         username_input.delete(0, END)
        #         password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("PassWord Manager")
screen.config(padx=50, pady=50)

screen_image = Canvas(width=200, height=200)
app_logo = PhotoImage(file="logo.png")
screen_image.create_image(100, 100, image=app_logo)
screen_image.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# inputs
website_input = Entry(width=36)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_input = Entry(width=36)
username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# button
password_button = Button(width=11, text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


screen.mainloop()