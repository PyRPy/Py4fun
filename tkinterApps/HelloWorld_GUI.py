import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox 

window = tk.Tk() 
my_lable = ttk.Label(window, text="Hello World!")
my_lable.grid(row=1, column=1) 
messagebox.showinfo("Info", "Informative message")
messagebox.showwarning("Warning", "Warning message")
window.mainloop() 
