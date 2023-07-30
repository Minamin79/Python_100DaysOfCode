from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(position)
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.goto(self.xcor(), (self.ycor() + 20))

    def down(self):
        self.goto(self.xcor(), (self.ycor() - 20))