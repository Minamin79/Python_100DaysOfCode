import random
from Hangman_art import *
from Hangman_words import word_list
from replit import clear
print(logo)

users_guessed_letters = []
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
lives = 6
game_ended = False

for letter in range(word_length):
    display.append('_')
print(display)

while not game_ended:
    guessed_letter = input('Guess a letter: ').lower()
    clear()

    if guessed_letter in users_guessed_letters:
        print(f'You\'ve already guessed this letter.')
        print(display)
    
    for position in range(word_length):
        letter = chosen_word[position]    
        if letter == guessed_letter:
            display[position] = letter
            users_guessed_letters.append(guessed_letter)
            print(display)
    
    if guessed_letter not in chosen_word and guessed_letter not in users_guessed_letters:
        lives -= 1
        if lives == 0:
            game_ended = True
            print(f'You Lose. The word was {chosen_word}.')
        else:
            print(f'You have {lives} left.')
            print(stages[lives])
            users_guessed_letters.append(guessed_letter)
            print(display)

    if '_' not in display:
        game_ended = True
        print('You win!')