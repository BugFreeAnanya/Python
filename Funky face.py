from turtle import *

class Face:
    def __init__(self, xpos, ypos):
        self.size=90
        self.coord=(xpos, ypos)
        self.noseSize="small"
    def setSize(self, radius):
        self.size=radius
    def goHome(self):
        penup()
        goto(self.coord)
        setheading(0)
    def drawOutline(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size)
        self.goHome()
    def drawEyes(self, turn):
        penup()
        left(turn)
        forward(self.size/2)
        pendown()
        dot(self.size/10)
        self.goHome()
    def drawMouth(self):
        penup()
        right(135)
        forward(self.size/1.7)
        left(90)
        pendown()
        circle(self.size/1.7, 90)
        self.goHome()
    def drawNose(self):
        if self.noseSize=="large":
            dot(self.size/2, "black")
        elif self.noseSize=="small":
            dot(self.size/6, "black")
        else:
            dot(self.size/4, "black")
        self.goHome()
    def draw(self):
        self.goHome()
        pensize(5)
        self.drawOutline()
        self.drawEyes(135)
        self.drawEyes(45)
        self.drawMouth()
        self.drawNose()

f1 = Face(0,0)
f1.draw()

showturtle()
done()