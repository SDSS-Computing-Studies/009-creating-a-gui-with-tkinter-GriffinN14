#! python3

# SD Computing Studies Assignment
#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Calculator")

label1 = tk.Label(window,text="X")

button1 = tk.Button(window,text="=")

entry1 = tk.Entry(window, borderwidth=1, relief=SUNKEN, width=10)

entry2 = tk.Entry(window, borderwidth=1, relief=SUNKEN, width=10)

entry3 = tk.Entry(window, borderwidth=1, relief=SUNKEN, width=18)

label1.grid(row = 1, column = 3)

button1.grid(row=1, column = 6)

entry1.grid(row=1, column = 1)

entry2.grid(row=1, column = 5)

entry3.grid(row=1, column = 8)

window.mainloop()
