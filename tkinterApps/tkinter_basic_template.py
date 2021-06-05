# tkinter example
from tkinter import *
def msg():
    print('hello stdout...')

top = Frame()
top.pack()
Label(top, text = 'Hello world').pack(side = TOP)
widget = Button(top, text = 'press', command = msg)
widget.pack(side = BOTTOM)
top.mainloop()

# from Python Pocket Reference, Mark Lutz 5th Ed
