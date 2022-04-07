import tkinter as tk 
from tkinter import filedialog 
import os 

app = tk.Tk() 
my_filetypes = [("all files", ".*"), ("text files", '.txt')] 

answer = filedialog.askdirectory(parent=app,
                                initialdir=os.getcwd(),  
                                title = "Please select a folder: ")

answer = filedialog.askopenfilename(parent=app, 
                                    initialdir=os.getcwd(), 
                                    title = "Please select a file: ", 
                                    filetypes=my_filetypes)

answer = filedialog.askopenfilenames(parent=app,
                                     initialdir=os.getcwd(),
                                     title="Please select one or more files:",
                                     filetypes=my_filetypes)

answer = filedialog.asksaveasfilename(parent=app,
                                      initialdir=os.getcwd(),
                                      title="Please select a file name for saving:",
                                      filetypes=my_filetypes)