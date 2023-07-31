from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
    
    def create_car(self):
        if random.randint(1, 6) == 6:
            new_car = Turtle()
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(290, random.randint(-240, 290))
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shape('square')
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def move_faster(self, user_score):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + user_score * MOVE_INCREMENT + 1)