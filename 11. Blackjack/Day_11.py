from art import logo
import random 
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

    
def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return 'You went over. You lose.'
    if user_score == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return 'Loser, opponent has Blackjack!'
    elif user_score == 0:
        return 'Win with a Blackjack!'
    elif user_score > 21:
        return 'You went over. You lose.'
    elif computer_score > 21:
        return 'Opponent went over. You win.'
    elif user_score > computer_score:
        return 'You win!'
    else:
        return 'You lose.'
    
    
def game():
    print(logo)

    user_cards = []
    comp_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_over:
        user_score = cal_score(user_cards)
        comp_score = cal_score(comp_cards)
        print(f'Your cards: {user_cards}, Current score: {user_score}')
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
    
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = cal_score(comp_cards)
    
    print(f'Your final hand: {user_cards}, Final score: {user_score}')
    print(f"Computer's final hand: {comp_cards}, Final score: {comp_score}")
    print(compare(user_score, comp_score))

        
        
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    game()
