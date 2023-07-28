# Snake game part 1
# The code works, but it will be completed and fully function on Day_21.

from turtle import Turtle, Screen
from snake import *
import time

snake = Snake()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

start_pos = [(0,0), (-20,0), (-40,0)]
for pos in start_pos:
    snake.add_tail(pos)
screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()