import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import pyclasp

window = Tk()

# Adjust size
window.geometry("1000x1000")


# Change the label text
def show():
    label.config(text=clicked.get())


# Dropdown menu options
options = [
    "Penality Logic",
    "Possibilistic Logic",
    "Qualitative Choice Logic"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Penality Logic")

# Create Dropdown menu
drop = OptionMenu(window, clicked, *options)
drop.pack()

# Create button, it will change label text
button = Button(window, text="choose", command=show).pack()

# Create Label
label = Label(window, text=" ")
label.pack()

# Execute tkinter
window.mainloop()


