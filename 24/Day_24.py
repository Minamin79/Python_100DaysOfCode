# Snake game part 3

from turtle import Screen
from very_completed_snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

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

snake.create_snake()
screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.add_tail_after_food()
        food.refresh()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    
    for sqr in snake.all_sqr:
        if sqr == snake.head:
            pass
        if sqr == snake.all_sqr[0]:
            pass
        elif snake.head.distance(sqr) < 5:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()