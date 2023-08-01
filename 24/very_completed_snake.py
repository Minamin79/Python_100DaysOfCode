from turtle import Turtle

class Snake:
    def __init__(self):
        self.start_pos = [(0,0), (-20,0), (-40,0)]
        self.all_sqr = []
        self.add_tail((0,0))
        self.head = self.all_sqr[0]

    def create_snake(self):
        for pos in self.start_pos:
            self.add_tail(pos)

    def add_tail(self, position):
        t = Turtle(shape='square')
        t.color('white')
        t.penup()
        t.goto(position)
        self.all_sqr.append(t)

    def add_tail_after_food(self):
        self.add_tail(self.all_sqr[-1].position())

    def move(self):
        for sqr_num in range(len(self.all_sqr)-1, 0, -1):
            new_x = self.all_sqr[sqr_num - 1].xcor()
            new_y = self.all_sqr[sqr_num - 1].ycor()
            self.all_sqr[sqr_num].goto(new_x, new_y)
            sqr_num = (new_x, new_y)
        self.head.forward(10)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for sqr in self.all_sqr:
            sqr.goto(1000, 1000)
        self.all_sqr.clear()
        self.create_snake()
        self.head = self.all_sqr[0]