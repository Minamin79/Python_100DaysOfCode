import random
from replit import clear
from game_data import data
from art import logo
# This code is a test of your understanding of different Instagram account followers. :)

print(logo)

def game():
    final_score  = 0

    chosen_a = random.choice(data)

    while True:
        chosen_b = random.choice(data)
        if chosen_a == chosen_b:
            chosen_b = random.choice(data)

        print(f"Compare A: {chosen_a['name']}, a {chosen_a['description']}, from {chosen_a['country']}.")
        print(f"Against B: {chosen_b['name']}, a {chosen_b['description']}, from {chosen_b['country']}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        clear()
        print(logo)

        while guess != 'a' and guess != 'b':
            print('Invald input')
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        correct_answer = chosen_a['follower_count'] > chosen_b['follower_count']
        if correct_answer and guess == 'a' or not correct_answer and guess == 'b':
            final_score  += 1
            
            print(f'Right answer! Current score: {final_score}')
            chosen_a = chosen_b

        else:
            print(f'Wrong answer. Your final score: {final_score}')
            break
    
game()
