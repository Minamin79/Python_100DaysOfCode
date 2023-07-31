from turtle import Screen
import time
from player import *
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('TurtleCross')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=player.up)

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_on = False
            
    if player.ycor() == FINISH_LINE_Y:
        player.goto(STARTING_POS)
        scoreboard.update_scoreboard()

screen.exitonclick()