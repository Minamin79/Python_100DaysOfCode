import turtle, pandas

screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guesses = []

while len(guesses) <50:
    answer = screen.textinput(title=f'{len(guesses)}/50 Guess the state', prompt="What's another state's name?").title()
    
    if answer == 'Exit':
        missing = []
        for state in all_states:
            if state not in guesses:
                missing.append(state)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv('states_to_learn.csv')
        break
        
    if answer in all_states:
        guesses.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


def get_mouse_click_cor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_cor)
turtle.mainloop()