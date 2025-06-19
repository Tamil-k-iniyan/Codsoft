from tkinter import *

window = Tk()
window.title("Contact Book")
window.geometry("500x500")

# Variables
name = StringVar()
phone = StringVar()
email = StringVar()

contacts = {}

# Functions
def add_contact():
    n = name.get()
    p = phone.get()
    e = email.get()
    if n and p and e:
        contacts[n] = [p, e]
        show_message(f"Added: {n} | {p} | {e}")
    else:
        show_message("Error: Please fill all fields")

def update_contact():
    n = name.get()
    if n in contacts:
        contacts[n] = [phone.get(), email.get()]
        show_message(f"Updated: {n} | {phone.get()} | {email.get()}")
    else:
        show_message("Error: Contact not found")

def delete_contact():
    n = name.get()
    if n in contacts:
        del contacts[n]
        show_message(f"Deleted contact: {n}")
    else:
        show_message("Error: Contact not found")

def search_contact():
    n = name.get()
    if n in contacts:
        phone.set(contacts[n][0])
        email.set(contacts[n][1])
        show_message(f"Found: {n} | {contacts[n][0]} | {contacts[n][1]}")
    else:
        show_message("Error: Contact not found")

def show_message(msg):
    result_box.insert(END, msg + "\n")
    result_box.see(END)  # Auto-scroll to latest message

# GUI layout
Label(window, text="Contact Book", font=("times new roman", 18)).grid(row=0, column=1, pady=10)

Label(window, text="Name:", font=("times new roman", 14)).grid(row=1, column=0, padx=20, pady=5, sticky=W)
Entry(window, textvariable=name, font=("times new roman", 14)).grid(row=1, column=1)

Label(window, text="Phone:", font=("times new roman", 14)).grid(row=2, column=0, padx=20, pady=5, sticky=W)
Entry(window, textvariable=phone, font=("times new roman", 14)).grid(row=2, column=1)

Label(window, text="Email:", font=("times new roman", 14)).grid(row=3, column=0, padx=20, pady=5, sticky=W)
Entry(window, textvariable=email, font=("times new roman", 14)).grid(row=3, column=1)

# Buttons
Button(window, text="Add", font=("Arial", 12), command=add_contact).grid(row=4, column=0, pady=10)
Button(window, text="Update", font=("Arial", 12), command=update_contact).grid(row=4, column=1)
Button(window, text="Delete", font=("Arial", 12), command=delete_contact).grid(row=5, column=0)
Button(window, text="Search", font=("Arial", 12), command=search_contact).grid(row=5, column=1)

# Result box (Text area)
Label(window, text="Result :", font=("Arial", 14)).grid(row=6, column=0, columnspan=2)
result_box = Text(window, height=10, width=50, font=("Courier", 10))
result_box.grid(row=7, column=0, columnspan=2, padx=20, pady=10)

window.mainloop()
