from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genterate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password = []
    for n in range(random.randint(8, 10)):
        password.append(random.choice(letters))
    for s in range(random.randint(2, 4)):
        password.append(random.choice(symbols))    
    for n in range(random.randint(2, 4)):
        password.append(random.choice(numbers))

    random.shuffle(password)
    
    random_pass = ''
    for char in password:
        random_pass += char
    password_entry.delete(0, END)
    password_entry.insert(0, random_pass)

# ---------------------------- Find PASSWORD ------------------------------- #
def find_pass():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except:
        messagebox.showerror(title=website, message='No data file found.')
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title='Error', message=f"No detail for {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) == 0 or len(email_username_entry.get()) == 10 or len(password_entry.get()) == 0:
            messagebox.showerror(message="You've left a field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=F'\
    These are the details entered:\n\
    Email: {email_username_entry.get()}\n\
    Password: {password_entry.get()}\n\
    Is it ok to save?')

        if is_ok:
            new_data = {website_entry.get(): {
                     'email': email_username_entry.get(),
                     'password': password_entry.get()
                }}
            
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
           
            except:
                 with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            
            finally:
                website_entry.delete(0, END)
                email_username_entry.delete(0, END)
                email_username_entry.insert(0, '@gmail.com')
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

website_label = Label(text='Website:')
website_label.grid(column=1, row=2)
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=2, row=2, columnspan=2)

email_username_label = Label(text='Email/username:')
email_username_label.grid(column=1, row=3)
email_username_entry = Entry(width=40)
email_username_entry.insert(0, '@gmail.com')
email_username_entry.grid(column=2, row=3, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(column=1, row=4)
password_entry = Entry(width=40)
password_entry.grid(column=2, row=4)
generate_password_button = Button(text='Generate password', command=genterate_pass, width=15)
generate_password_button.grid(column=4, row=4, columnspan= 1)

add_button = Button(text='Add',command=save , width=34)
add_button.grid(column=2, row=5, columnspan= 2)

search_button = Button(text='Search', command=find_pass, width=15)
search_button.grid(column=4, row=2, columnspan= 1)

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=2, row=1)


window.mainloop()
