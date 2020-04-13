# matplotlib_tkinter.py
# ref https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html
import tkinter 
from matplotlib.backends.backend_tkagg import(
    FigureCanvasTkAgg, NavigationToolbar2Tk
)

from matplotlib.backend_bases import key_press_handler 
from matplotlib.figure import Figure 

import numpy as np 

root = tkinter.Tk() 
root.wm_title("Embedding in Tk")

fig = Figure(figsize = (5,4), dpi=100)
t = np.arange(0,3, 0.01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t)) 

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw() 
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = 1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect("key_press_event", on_key_press)

def _quit():
    root.quit()
    root.destroy() 

button = tkinter.Button(master = root, text = 'quit', command = _quit)
button.pack(side = tkinter.BOTTOM)

tkinter.mainloop()