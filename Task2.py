from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("500x400")

num1 = IntVar()
num2 = IntVar()

l = Label(window,text = "Simple Calculator",font = ("times new roman",16))
l.grid(row = 0,column = 1,padx = 10)

l1 = Label(window,text = "Number1 :",font = ("times new roman",16))
l1.grid(row=1,column=0,padx = 20,pady = 30)
e1 = Entry(window,textvariable = num1,font = ("times new roman",16))
e1.grid(row = 1,column = 1 )

l2 = Label(window,text = "Number2 :",font = ("times new roman",16))
l2.grid(row=2,column=0)
e2 = Entry(window,textvariable = num2,font = ("times new roman",16))
e2.grid(row = 2,column = 1)

def add():
    add = num1.get()+num2.get()
    result.config(text = f"Result : {add}")
def sub():
    sub = num1.get()-num2.get()
    result.config(text = f"Result : {sub}")
def mul():
    mul = num1.get()*num2.get()
    result.config(text = f"Result : {mul}")

def div():
    if num2.get() == 0:
        result.config(text = f"Error!!Try Again")
    else:
        div = num1.get()/num2.get()
        result.config(text = f"Result :{div}")


result = Label(window,text = " ",font = ("Arial",16))
result.grid(row = 4,column = 1)

b1 = Button(window,text= "+",font = ("Arial",16),command = add)
b1.grid(row = 3,column = 1,pady = 20,sticky = NW)

b2 = Button(window,text= "-",font = ("Arial",16),command = sub)
b2.grid(row = 3,columnspan = 1,pady = 20,sticky = N)

b3 = Button(window,text= "*",font = ("Arial",16),command = mul)
b3.grid(row = 3,column = 1,pady = 20,sticky = E)

b4 =Button(window,text= "/",font = ("Arial",16),command = div)
b4.grid(row = 3,column = 1,pady = 20,sticky = S)


window.mainloop()