from replit import clear
from art import logo

print(logo)
print('Welcome to the secret auction program.')
off = False
bidder_and_bids = {}

def find_highest_bidder(bidding_record):
    highest = 0
    winner = ''
    for bidders in bidding_record:
        bid_amount = bidding_record[bidders]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidders 
    print(f'The winner is {winner} with the bid of {highest}.')

while not off:
    try:
        name = input('What is your name? ')
        bid = int(input("What's your bid? $"))
        other_biders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

        bidder_and_bids[name] = bid

        while other_biders != 'yes' and other_biders != 'no':
            print('Invalid data.')
            other_biders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()     
        if other_biders == 'yes':
            clear()
        elif other_biders == 'no':
            find_highest_bidder(bidder_and_bids)
            off = True
    except:
        print('Invalid data')
