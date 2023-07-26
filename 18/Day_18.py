import random
from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape('turtle')
# timmy.pensize(15)
timmy.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

timmy.pencolor(random_color())
timmy.circle(100)

screen = Screen()
screen.exitonclick()