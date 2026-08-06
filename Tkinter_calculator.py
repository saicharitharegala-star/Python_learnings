import math
from tkinter import *
 
window = Tk()
window.geometry("500x500")
window.title("Calculator")

e = Entry(window, width=50, borderwidth=5)
e.place(x = 0 , y = 0)

def click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

number_positions = [
    (1, 10, 60), (2, 140, 60), (3, 270, 60),
    (4, 10, 120), (5, 140, 120), (6, 270, 120),
    (7, 10, 180), (8, 140, 180), (9, 270, 180),
    (0, 140, 240),
]

for digit, x, y in number_positions:
    button = Button(window, text=str(digit), width=10,
                    command=lambda digit=digit: click(digit))
    button.place(x=x, y=y)
def add():
    first_number = e.get()
    global math 
    global n1
    math = "addition"
    n1 = int(first_number)
    e.delete(0,END)

b = Button(window, text = "+", width = 10, command=add)
b.place(x = 10, y =240)

def sub():
    first_number = e.get()
    global math
    global n1
    math = "subtraction"
    n1 = int(first_number)
    e.delete(0,END)

b = Button(window, text = "-", width = 10, command=sub)
b.place(x = 270, y =240)

def mul():
    first_number = e.get()
    global math
    global n1
    math = "multiplication"
    n1 = int(first_number)
    e.delete(0,END)

b = Button(window, text = "*", width = 10, command=mul)
b.place(x = 10, y =300)

def div():
    first_number = e.get()
    global math
    global n1
    math = "division"
    n1 = int(first_number)
    e.delete(0,END)

b = Button(window, text = "/", width = 10, command=div)
b.place(x = 270, y =300)

def equal():
    second_number = e.get()
    global n1
    n2 = int(second_number)
    e.delete(0,END)
    if math == "addition":
        e.insert(0, n1 + n2)
    elif math == "subtraction":
        e.insert(0, n1 - n2)
    elif math == "multiplication":
        e.insert(0, n1 * n2)
    elif math == "division":
        e.insert(0, n1 / n2)

b = Button(window, text = "=", width = 10, command=equal)
b.place(x = 140, y =300)

def clear():
    e.delete(0,END)

b = Button(window, text = "clear", width = 10, command=clear)
b.place(x = 140, y =360)
window.mainloop()
