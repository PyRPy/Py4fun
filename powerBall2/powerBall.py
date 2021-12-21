# https://ineasysteps.com/products-page/python-in-easy-steps/
# this example is adapted from the book listed above
from tkinter import *
from random import sample
import datetime
today = str(datetime.date.today())

window = Tk()
img = PhotoImage(file = 'powerBall.png')

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
savBtn = Button(window)

# manage the layout
imgLbl.grid(row = 1, column = 1, rowspan = 2)
label1.grid(row = 1, column = 2, padx = 10)
label2.grid(row = 1, column = 3, padx = 10)
label3.grid(row = 1, column = 4, padx = 10)
label4.grid(row = 1, column = 5, padx = 10)
label5.grid(row = 1, column = 6, padx = 10)
label6.grid(row = 1, column = 7, padx = (10, 20))
getBtn.grid(row = 2, column = 2, columnspan = 2)
savBtn.grid(row = 2, column = 4, columnspan= 2)
resBtn.grid(row = 2, column = 6, columnspan = 2)

# static properties
window.title('Power Ball Number Picker')
window.resizable(0, 0)
getBtn.configure(text = 'Play')
resBtn.configure(text = 'Reset')
savBtn.configure(text = 'Save')

# initial properties
label1.configure(text = '...')
label2.configure(text = '...')
label3.configure(text = '...')
label4.configure(text = '...')
label5.configure(text = '...')
label6.configure(text = '...')

resBtn.configure(state = DISABLED) # from start
savBtn.configure(state = DISABLED) # from start

# Dynamic properties
# nums_white = []
# nums_red =[]

def pick():
	global nums_white
	global nums_red
	nums_white = sample(range(1, 70), 5) # select 5 white balls from 69 balls
	nums_red = sample(range(1, 27), 1)
	label1.configure(text = nums_white[0])
	label2.configure(text = nums_white[1])
	label3.configure(text = nums_white[2])
	label4.configure(text = nums_white[3])
	label5.configure(text = nums_white[4])

	label6.configure(text = nums_red[0])
	getBtn.configure(state = DISABLED)
	resBtn.configure(state = NORMAL)
	savBtn.configure(state = NORMAL)

def reset():
	label1.configure(text = '...')
	label2.configure(text = '...')
	label3.configure(text = '...')
	label4.configure(text = '...')
	label5.configure(text = '...')
	label6.configure(text = '...')
	getBtn.configure(state = NORMAL)
	resBtn.configure(state = DISABLED)
	savBtn.configure(state = DISABLED)

# save the numbers generated
def saveNums():
	nums_string = str(nums_white[0]) + ' ' + str(nums_white[1]) + ' ' + \
				  str(nums_white[2]) + ' ' + str(nums_white[3]) + ' ' + \
				  str(nums_white[4]) + ' ' + str(nums_red[0])
	
	nums_string = today + ': ' + nums_string
	file = open("numbers.txt", 'a')
	file.write(nums_string + '\n')

# nominate relevant function to be called when Botton is pressed
getBtn.configure(command = pick)
resBtn.configure(command = reset)
savBtn.configure(command = saveNums)

# test code for saving numbers

# sustain window
window.mainloop()