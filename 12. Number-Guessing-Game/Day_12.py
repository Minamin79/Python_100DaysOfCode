import random
from replit import clear

print("Welcome to the Number Guessing Game!\n\
I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def game():
    chosen_number = random.randint(0, 101)
    
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
    print(f'You have {attempts} attempts remaining to guess the number.')

    try:
        while attempts > 0:
            try:
                guess = int(input('Make a guess: '))
            except:
                print("Invalid input! Please enter number.")
                continue
            else:
                if guess > chosen_number:
                    clear()
                    print('Too high\nGuess again.')
                    attempts -= 1
                    print(f'You have {attempts} attempts remaining to guess the number.')
                elif guess < chosen_number:
                    clear()
                    print('Too low\nGuess again.')
                    attempts -= 1
                    print(f'You have {attempts} attempts remaining to guess the number.')
                else:
                    print(f'You got it! The answer was {chosen_number}.')
                    return
            if attempts == 0:
                print(f"You've ran out of guesses, you lose.\nThe number was: {chosen_number}.")
                return
    except:
            print('Invalid input')


while difficulty != 'easy' and difficulty != 'hard':
    print('Invalid input.')
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
game()
