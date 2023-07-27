from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
bet = screen.textinput(title='Make your bet', prompt='Which tutle will win the race? ').lower()
all_turtles = []
y_pos = 105
race_on = False

while bet not in colors:
    print('Invalid input.')
    bet = screen.textinput(title='Make your bet', prompt='Which tutle will win the race? ').lower()
else:
    pass

for o in range(6):
    i = Turtle(shape='turtle')
    i.color(colors[o-1])
    i.penup()
    i.goto(x=-230, y=y_pos-(40 * o))
    all_turtles.append(i)
    
if bet:
    race_on = True
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            print(winner)
            if winner == bet:
                print('Your turtle won!')
            else:
                print(f"Sorry, the {winner} turtle won.")
            race_on = False
        rand_dis = random.randint(1, 10)
        turtle.forward(rand_dis)
        
screen.exitonclick()