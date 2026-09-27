from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
    def writes(self,level):
        self.clear()
        if level==0:
            self.goto(0,0)
            self.write("gameover")
        else:
             self.goto(-270,270)
             self.write(arg=f"Level:{level}",move=False)