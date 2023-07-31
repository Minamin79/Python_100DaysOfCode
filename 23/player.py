from turtle import Turtle

STARTING_POS = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POS)
        self.shape('turtle')
        self.color('green')
    
    def up(self):
        self.forward(MOVE_DISTANCE)