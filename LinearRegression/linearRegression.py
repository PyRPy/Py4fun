# linearRegression.py

from graphics import * 
# these two 'constants' are defined here so they can be used in multiple
# functions to draw the done button and check to see if it is clicked in

DoneX = 1.0 # x coord. of done button upper right 
DoneY = 0.75 # y coord. of done button upper right 

class Regression:

    def __init__(self):
        self.sumx = 0.0 
        self.sumy = 0.0 
        self.sumxx = 0.0
        self.sumxy = 0.0 
        self.n = 0 

    def addPoint(self, x, y):
        self.sumx = self.sumx + x 
        self.sumy = self.sumy + y 
        self.sumxx = self.sumxx + x*x 
        self.sumxy = self.sumxy + x*y 
        self.n =  self.n + 1 

    def predict(self, x):
        xbar = self.sumx / self.n 
        ybar = self.sumy / self.n 
        slope = ((self.sumxy - self.n * xbar * ybar) / (self.sumxx - self.n * xbar * xbar)) 
        return ybar + slope * (x - xbar) 

def createWindow():
    win = GraphWin("linear regression", 500, 500) 
    win.setCoords(0,0,10,10)
    button = Rectangle(Point(0.05, 0), Point(DoneX, DoneY)) 
    text = Text(Point(DoneX/2.0, DoneY/2.0), "Done")
    text.draw(win)
    button.draw(win)
    return win 

def getPoints(win):
    reg = Regression() 
    pt = getPoint(win)
    while pt != None:
        reg.addPoint(pt.getX(), pt.getY())
        pt = getPoint(win) 
    return reg 

def getPoint(w):
    p1 = w.getMouse()
    if isDoneButton(p1):
        return None 
    else:
        p1.draw(w) 
        return p1 

def isDoneButton(p):
    return p.getX() <= DoneX and p.getY() <= DoneY

def main():
    # create a window, and allow user to click points
    win = createWindow() 
    regressor = getPoints(win) 

    # calculate line of best fit 
    y1 = regressor.predict(0) 
    y2 = regressor.predict(10) 

    # draw the line 
    regLine = Line(Point(0,y1), Point(10, y2)) 
    regLine.setWidth(2) 
    regLine.draw(win) 

    # close up shop 
    win.getMouse()
    win.close()

main() 

