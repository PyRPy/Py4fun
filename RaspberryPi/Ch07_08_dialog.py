# dialogs
from tkinter import *
import tkinter.messagebox as mb

class App:
	def __init__(self, master):
		b = Button(master, text='Press Me', command=self.info).pack()
		
	def info(self):
		mb.showinfo('Information', "please don't press that button again")
		
root = Tk()
app = App(root)
root.mainloop()