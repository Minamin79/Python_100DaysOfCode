#ASCII art: https://ascii.co.uk/art/treasure
# You will choose your path through the given choices and make your own story. Let's see if you can survive!

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print('Welcome to Treasure Island.\nYour mission is to find the treasure.')

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == 'left':
    choice2 = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across..\n').lower()
    if choice2 == 'wait':
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n').lower()
        if choice3 == 'yellow':
            print('YOU FOUND THE TREASURE! YOU WIN!')
        elif choice3 == 'red':
            print('It\'s a room full of fire. GAME OVER!')
        elif choice3 == 'blue':
            print('You entered a room full of beasts. GAME OVER!')
        else:
            print('Invalid input!')
    elif choice2 == 'swim':
            print('You got attacked by a shark. GAME OVER!')
    else:
        print('Invalid input!')
elif choice1 == 'right':
    print('You fell into a hole. GAME OVER!')
else:
    print('Invalid input!')