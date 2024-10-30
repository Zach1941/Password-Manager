import tkinter
from tkinter import PhotoImage, messagebox
import string
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

"""
this generates a password for the user using random characters that's 14 characters 
long
"""
def generating_password():
    generated_password =[]
    for n in range (0,12):
        random_letter =random.choice(string.ascii_letters)
        generated_password.append(str(random_letter))
        random_number = random.randint(0, 9)
        if random_number%2 == 0:
            generated_password.append(str(random_number))

    random.shuffle(generated_password)
    password_entry.insert( index = 0, string=f"{("".join(generated_password))}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

"""
this saves the password to a txt file
"""
def saving_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data ={
        website: {
            "email": email,
            "password": password,

        }
    }

    if len(password_entry.get()) == 0 or len(website_entry.get()) ==  0:
        messagebox.showerror(title = "warning", message = "error website or password field is empty")
    else:
        try:
            with open("password_manager.json", mode = 'r') as saved_passwords:
                # noinspection PyTypeChecker
                data = json.load(saved_passwords)
                data.update(new_data)


            with open ("password_manager.json", mode = 'w') as saved_passwords:
                # noinspection PyTypeChecker
                json.dump(data, saved_passwords, indent=4)


        except FileNotFoundError:
            with open("password_manager.json", mode='w') as saved_passwords:
                # noinspection PyTypeChecker
                json.dump(new_data, saved_passwords, indent = 4)
        finally:
            website_entry.delete(0, len(website))
            password_entry.delete(0, len(password))
# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("password_manager.json") as saved_passwords:
            data = json.load(saved_passwords)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title = website, message = f"email: {email}\n"
                                                               f"password = {password}")
            else:
                messagebox.showinfo(title="no data found", message = "sorry data not found please try again")
    except FileNotFoundError:
        messagebox.showinfo(title = "no data found",message = "you have not saved any passwords yet" )



# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("LegendPass password manager")
window.config(padx = 20, pady = 20)

logo = PhotoImage(file ="LegendPass_Logo.png")

canvas = tkinter.Canvas(height = 200, width = 315)
canvas.create_image(170, 110, image = logo)
canvas.grid(column = 1, row = 1)

website_label = tkinter.Label(text = "website: ")
website_label.grid(column = 0, row = 2 )

search_button = tkinter.Button(text = "search", command = find_password)
search_button.grid(column = 2, row = 2)

website_entry = tkinter.Entry(width = 35)
website_entry.grid(column = 1 , row= 2)
website_entry.focus()

email_label = tkinter.Label(text = "Email/Username: ")
email_label.grid(column = 0, row = 3)

email_entry = tkinter.Entry(width = 35)
email_entry.grid(column =1 , row =3)

password_label = tkinter.Label(text ="Password: ")
password_label.grid(column =0, row = 4 )

password_entry = tkinter.Entry( width = 35)
password_entry.grid(column = 1, row = 4)

generate_button = tkinter.Button(text = "Generate Password", command = generating_password)
generate_button.grid(column =2 , row = 4,)

add_button = tkinter.Button(text = "Add", width = 36, command = saving_password)
add_button.grid(column =1, row =5 )




window.mainloop()