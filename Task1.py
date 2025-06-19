from tkinter import *

window = Tk()
window.title("To-Do List")
window.geometry("500x400")

tasks = []

def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()

def clear_tasks():
    tasks.clear()
    update_listbox()

def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index] = f"{tasks[index]} ✔️"
        update_listbox()

title = Label(window, text="To-Do List", font=("times new roman", 20))
title.grid(row=0, column=1, pady=10)

entry = Entry(window, width=30, font=("times new roman", 16))
entry.grid(row=1, column=1, padx=10, pady=10)

add_btn = Button(window, text="Add Task", font=("Arial", 14), command=add_task)
add_btn.grid(row=2, column=0, padx=10, pady=5)

delete_btn = Button(window, text="Delete Task", font=("Arial", 14), command=delete_task)
delete_btn.grid(row=2, column=1, padx=10, pady=5, sticky=W)

mark_btn = Button(window, text="Mark as Done", font=("Arial", 14), command=mark_done)
mark_btn.grid(row=2, column=1, padx=10, pady=5, sticky=E)

clear_btn = Button(window, text="Clear All", font=("Arial", 14), command=clear_tasks)
clear_btn.grid(row=2, column=2, padx=10, pady=5)

listbox = Listbox(window, width=40, height=10, font=("times new roman", 14))
listbox.grid(row=3, column=0, columnspan=3, padx=20, pady=20)

window.mainloop()
