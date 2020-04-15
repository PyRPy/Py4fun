# tkinter_photo_text.py
from tkinter import *
root = Tk()
root.geometry('200x300')
v = IntVar() 
Label(root, root.title('Options'), text="--- Choose a preferred language ---", justify = LEFT,
padx = 20).pack()

Radiobutton(root, 
    text = "Python", 
    padx = 20,
    variable = v, 
    value = 1).pack(anchor=W)

Radiobutton(root, 
    text = "C++", 
    padx = 20,
    variable = v, 
    value = 2).pack(anchor=W)

txt = ""
if v.get() == 0:
    txt = "Python is selected"
if v.get() == 1:
    txt = "C++ is selected"
Label(root, text = txt, justify = RIGHT, padx = 20).pack()
print(v.get())

mainloop() 
