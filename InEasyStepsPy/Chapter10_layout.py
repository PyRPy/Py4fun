# widget

from tkinter import *
window = Tk()
img = PhotoImage(file = 'logo.gif')

# create widgets
imgLbl = Label(window, image = img)
label1 = Label(window, relief='groove', width = 2)
label2 = Label(window, relief='groove', width = 2)
label3 = Label(window, relief='groove', width = 2)
label4 = Label(window, relief='groove', width = 2)
label5 = Label(window, relief='groove', width = 2)
label6 = Label(window, relief='groove', width = 2)
getBtn = Button(window)
resBtn = Button(window)

# manage the layout
imgLbl.grid(row = 1, column = 1, rowspan = 2)
label1.grid(row = 1, column = 2, padx = 10)
label2.grid(row = 1, column = 3, padx = 10)
label3.grid(row = 1, column = 4, padx = 10)
label4.grid(row = 1, column = 5, padx = 10)
label5.grid(row = 1, column = 6, padx = 10)
label6.grid(row = 1, column = 7, padx = (10, 20))
getBtn.grid(row = 2, column = 2, columnspan = 2)
resBtn.grid(row = 2, column = 6, columnspan = 2)

# sustain window
window.mainloop()