#! python3

# SD Computing Studies Assignment
#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

dogphoto = PhotoImage(file="dog.png")

label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="Pochacco!")
label3 = tk.Label(window, text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg="light blue")

label1.grid(row = 1, column = 2,rowspan = 4)
label2.grid(row = 2, column = 3, sticky = "SW")
label3.grid(row = 5, column = 1, columnspan = 3)

window.mainloop()
