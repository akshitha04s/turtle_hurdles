from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.restart()
    def restart(self):
        self.goto(0,-280)
        self.setheading(90)
    def goup(self):
        self.forward(10)