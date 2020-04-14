# matplotlib_tkinter2.py
# ref : https://stackoverflow.com/questions/25498937/embed-a-pyplot-in-a-tkinter-window-and-update-it

import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfile 
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

root = tk.Tk()

fig = plt.figure(1)
t = np.arange(0.0,3.0,0.01)
s = np.sin(np.pi*t)
plt.plot(t,s)

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

# read csv files
def open_file():
    file = askopenfile(mode='r', filetypes = [('csv files', '*.csv')])
    if file is not None:
        data = pd.read_csv(file)
        x = data['Time']
        y = data['Count']
        plt.clf() # clear plot first
        plt.plot(x, y)
        plt.xlabel('Time')
        plt.ylabel('Count')
        # plt.draw()
        # fig.canvas.draw() 
 

tk.Button(root, text='Open', command = open_file).grid(row=2, column=1)

def update():
    fig.canvas.draw() 

def _quit():
    root.quit()
    root.destroy()  # correction: to clean the window when exit

plot_widget.grid(row=0, column=0)
tk.Button(root,text="Update",command=update).grid(row=1, column=0)

# add a quit button below 'update' button
tk.Button(root, text = 'Quit', command = _quit).grid(row=2, column=0)

root.mainloop()