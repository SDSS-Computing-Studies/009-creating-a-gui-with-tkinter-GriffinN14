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

label2 = tk.Label(window, text="Name")
label3 = tk.Label(window, text="Type")
label4 = tk.Label(window, text="Breed")
label5 = tk.Label(window, text="Owner")
label6 = tk.Label(window, text="Birthdate")
label7 = tk.Label(window, text="Client Database")

button1 = tk.Button(window,text="Search by Name")
button2 = tk.Button(window,text="Save Entry")
button3 = tk.Button(window,text="Next >")
button4 = tk.Button(window,text="< Previous")

entry1 = tk.Entry(window, borderwidth=1, width=12)

entry2 = tk.Entry(window, borderwidth=1, width=12)

entry3 = tk.Entry(window, borderwidth=1, width=12)

entry4 = tk.Entry(window, borderwidth=1, width=12)

entry5 = tk.Entry(window, borderwidth=1, width=12)

entry6 = tk.Entry(window, borderwidth=1, width=10)

label1.grid(row = 1, column = 1,rowspan = 4)
label2.grid(row = 5, column = 1)
label3.grid(row = 5, column = 2)
label4.grid(row = 5, column = 3)
label5.grid(row = 5, column = 5)
label6.grid(row = 5, column = 6)
label7.grid(row = 2, column = 3)

button1.grid(row=1, column = 5)
button2.grid(row=7, column = 3)
button3.grid(row=7, column = 6,sticky="E")
button4.grid(row=7, column = 1)

entry1.grid(row=6, column = 1)

entry2.grid(row=6, column = 2)

entry3.grid(row=6, column = 3)

entry4.grid(row=6, column = 5)

entry5.grid(row=6, column = 6)

entry6.grid(row=1, column = 6, columnspan=7)

window.mainloop()
