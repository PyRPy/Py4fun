# draw lines using turtle
from turtle import *
instructions = "GGLLGG"
space = Screen()
space.title("draw circles")
angle = 90
unit = 100 
robot = Turtle()

for letter in instructions:
    if letter == "G":
        robot.forward(unit)
    if letter == "L":
        robot.left(angle) 
        robot.forward(unit)
    if letter == "R":
        robot.right(angle)
        robot.forward(unit)

robot.done()