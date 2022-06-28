from tkinter import *

window = Tk()
window.config(padx=50, pady=50)

window.title("Password Manager")

#functions

def save():
    website_save = website_input.get()
    email_save = email_input.get()
    password_save = password_input.get()
    f = open("data_files", "a")
    f.write(f"{website_save} | {email_save} | {password_save},\n")
    f.close()

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
generate_button = Button(text="Generate")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")




window.mainloop()