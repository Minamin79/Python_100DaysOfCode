from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Ping-Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=r_paddle.up)
screen.onkey(key='Down', fun=r_paddle.down)
screen.onkey(key='w', fun=l_paddle.up)
screen.onkey(key='s', fun=l_paddle.down)

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.add_r_score()

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.add_l_score()


screen.exitonclick()