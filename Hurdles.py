from turtle import Turtle
import random as r
colors=["red","blue","yellow","black","purple","pink","green","orange"]
h=[]
speed=10
class Hurdles():
    def __init__(self):
        pass
    def create(self):
        if r.randint(1,6)==1:
                  yy=r.randint(-250,250)
                  f=Turtle()
                  f.shape("square")
                  f.penup()
                  f.shapesize(1,2,1)
                  f.goto(280,yy)
                  f.color(r.choice(colors))
                  h.append(f)
    def moveback(self):
        for hurd in h:
            hurd.backward(speed)