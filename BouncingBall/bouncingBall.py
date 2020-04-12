# bouncingBall.py
from tkinter import * 
import random 
import time 
from ball import *
from paddle import * 

# create game canvas 
tk = Tk() 
tk.title("Ball can bounce !")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1) 
canvas = Canvas(tk, width = 500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

# make the ball bounce and hit the ball
while 1:
    if ball.hit_bottom == False:
        ball.draw() 
        paddle.draw() 
    tk.update_idletasks() 
    tk.update() 
    time.sleep(0.02) 


