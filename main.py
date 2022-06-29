from tkinter import *
from tkinter import messagebox
import random
import pyperclip

window = Tk()
window.config(padx=50, pady=50)

window.title("Password Manager")

#functions

def generate():
    password_input.delete(0,END)
    password = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)

    # for char in password_list:
    #     password += char

    password_input.insert(0,password)



def save():
    website_save = website_input.get()
    email_save = email_input.get()
    password_save = password_input.get()

    if website_save == "" or password_save == "":
        messagebox.showinfo(title="warning", message="You shouldn't let any field empty !!!")

    else:
        #message box
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nEmail: {email_save}\nPassword: {password_save}\nIs it ok for save?")

        if is_ok:
            with open("data_files", "a") as data_file:
                data_file.write(f"{website_save} | {email_save} | {password_save},\n")
            website_input.delete(0,"end")
            password_input.delete(0,"end")

#Image
canvas = Canvas(width=200, height=200)
safe_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=safe_img)
canvas.grid(row=0, column=1)


#labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Entries

website_input = Entry(width=52)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)


email_input = Entry(width=52)
email_input.insert(0,"altoullec@yahoo.fr")
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=32)
password_input.grid(column=1, row=3, sticky="W")


#Buttons
generate_button = Button(text="Generate", command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")




window.mainloop()