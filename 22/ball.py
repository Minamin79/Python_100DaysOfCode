from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('pink')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(x=(self.xcor() + self.x_move), y=(self.ycor() + self.y_move))

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1