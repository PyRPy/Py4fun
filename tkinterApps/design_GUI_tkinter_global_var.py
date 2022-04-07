import tkinter as tk 
from tkinter import ttk 

global my_counter 

def create_user_interface(app_window):
    global my_counter 
    my_counter = ttk.Label(app_window, text="0")
    my_counter.grid(row=0, column=0) 

    increment_button = ttk.Button(app_window, text="Add 1 to counter") 
    increment_button.grid(row=1, column=0) 
    increment_button['command'] = increment_counter 

    quit_button = ttk.Button(app_window, text="Quit")
    quit_button.grid(row=2, column=0)
    quit_button['command'] = window.destroy

def increment_counter():
    global my_counter 
    my_counter['text'] = str(int(my_counter['text']) + 1)

# create main window
window = tk.Tk() 
create_user_interface(window)

# start GUI event loop
window.mainloop() 