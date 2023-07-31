from turtle import Turtle

FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('Black')
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write(self.score, align='center', font=FONT)     

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(self.score, align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=FONT)