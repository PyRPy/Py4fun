# read csv files through tkinter dialog window
from tkinter import * 
from tkinter.ttk import * 

from tkinter.filedialog import askopenfile 
import pandas as pd

root = Tk()
root.geometry('200x100')

def open_file():
    file = askopenfile(mode='r', filetypes = [('csv files', '*.csv')])
    if file is not None:
        content = pd.read_csv(file)
        print(content.head()) # this will print in the terminal

btn = Button(root, text='open', command = open_file)
btn.pack(side = TOP, pady = 10)

mainloop() 
