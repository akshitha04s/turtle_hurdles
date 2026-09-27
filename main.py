from turtle import Screen
import time
import Player
import Scoreboard
import Hurdles
screen=Screen()
screen.setup(600,600)
les=screen.textinput("welcome to turtle hurdles","shall we start")
screen.tracer(0)
player=Player.Player()
hurdles=Hurdles.Hurdles()
score=Scoreboard.Scoreboard()
level=1
score.writes(level)
screen.listen()
screen.onkey(player.goup,"Up")
gameon=True
while gameon:
    time.sleep(0.1)
    hurdles.create()
    hurdles.moveback()
    if player.ycor()>=280:
        level+=1
        score.writes(level)
        Hurdles.speed+=10
        player.restart()
    for hurd in Hurdles.h:
        if player.distance(hurd)<20:
            level=0
            score.writes(0)
            gameon=False
    screen.update()