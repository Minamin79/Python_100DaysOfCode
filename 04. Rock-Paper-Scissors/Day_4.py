import random

rock = \
'''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ 

'''

paper = \
'''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''

scissors = \
'''
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \ 
|___/\___|_|___/___/\___/|_|  |___/
'''

user_choice = input('What do you choose? Type "Rock", "Paper" or "Scissors"\n').lower()
computer_choice = random.choice(['rock', 'paper', 'scissors'])

if user_choice == computer_choice:
    print('Draw')
elif user_choice == 'rock' and computer_choice == 'paper':
    print(rock)
    print('Computer chose:\n', paper)
    print('Computer wins') 
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(rock)
    print('Computer chose:\n', scissors)
    print('You win') 
elif user_choice == 'paper' and computer_choice == 'rock':
    print(paper)
    print('Computer chose:\n', rock)
    print('You win') 
elif user_choice == 'paper' and computer_choice == 'scissors':
    print(paper)
    print('Computer chose:\n', scissors)
    print('Computer wins') 
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(scissors)
    print('Computer chose:\n', paper)
    print('You win') 
elif user_choice == 'scissors' and computer_choice == 'rock':
    print(scissors)
    print('Computer chose:\n', rock)
    print('Computer wins') 
else:
    print('Invalid input')

