import tkinter as tk 
from tkinter import simpledialog 

app = tk.Tk() 
answer = simpledialog.askstring("Input", "What is your first name?", parent = app) 

if answer is not None:
    print("your first name is ", answer)
else:
    print("your don't have a first name?") 

answer = simpledialog.askinteger("Input", "what is your age?",
                                  parent = app, 
                                  minvalue = 0, maxvalue = 100)

if answer is not None: 
    print("your age is ", answer) 
else:
    print("your don't have an age?")

answer = simpledialog.askfloat("Input", "What is your salary?",
                               parent=app,
                               minvalue=0.0, maxvalue=100000.0)

if answer is not None: 
    print("your age is ", answer) 
else:
    print("your don't have a salary?")