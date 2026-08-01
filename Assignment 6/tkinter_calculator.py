import math
from tkinter import *
 
# Create the main application window
window = Tk()
window.geometry("500x500")
window.title("Calculator")

# Entry widget for displaying input and results
e = Entry(window, width=50, borderwidth=5)
e.place(x = 0 , y = 0)

# Appends the pressed digit to the current entry text
def click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

# Number buttons
b = Button(window, text = "1", width = 10, command=lambda: click(1))
b.place(x = 10, y =60)

b = Button(window, text = "2", width = 10, command=lambda: click(2))
b.place(x = 140, y =60)

b = Button(window, text = "3", width = 10, command=lambda: click(3))
b.place(x = 270, y =60)

b = Button(window, text = "4", width = 10, command=lambda: click(4))
b.place(x = 10, y =120)

b = Button(window, text = "5", width = 10, command=lambda: click(5))
b.place(x = 140, y =120)

b = Button(window, text = "6", width = 10, command=lambda: click(6))
b.place(x = 270, y =120)

b = Button(window, text = "7", width = 10, command=lambda: click(7))
b.place(x = 10, y =180)

b = Button(window, text = "8", width = 10, command=lambda: click(8))
b.place(x = 140, y =180)

b = Button(window, text = "9", width = 10, command=lambda: click(9))
b.place(x = 270, y =180)

b = Button(window, text = "0", width = 10, command=lambda: click(0))
b.place(x = 140, y =240)

# Store the first number and selected operation
def add():
    first_number = e.get()
    global math 
    global n1
    math = "addition"
    n1 = int(first_number)
    e.delete(0,END)

b = Button(window, text = "+", width = 10, command=add)
b.place(x = 10, y =240)

# Prepare subtraction operation
def sub():
    first_number = e.get()
    global math
    global n1
    math = "subtraction"
    n1 = int(first_number)
    e.delete(0,END)

b = Button(window, text = "-", width = 10, command=sub)
b.place(x = 270, y =240)

# Prepare multiplication operation
def mul():
    first_number = e.get()
    global math
    global n1
    math = "multiplication"
    n1 = int(first_number)
    e.delete(0,END)

b = Button(window, text = "*", width = 10, command=mul)
b.place(x = 10, y =300)

# Prepare division operation
def div():
    first_number = e.get()
    global math
    global n1
    math = "division"
    n1 = int(first_number)
    e.delete(0,END)

b = Button(window, text = "/", width = 10, command=div)
b.place(x = 270, y =300)

# Calculate the result based on stored operation
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

# Clear the entry field
def clear():
    e.delete(0,END)

b = Button(window, text = "clear", width = 10, command=clear)
b.place(x = 140, y =360)

# Start the Tkinter event loop
window.mainloop()