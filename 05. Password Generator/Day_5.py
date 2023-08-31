import random
# This code will generate a secure and random password for you. You can choose how many letters, symbols and numbers you want in your password too.

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print('Welcome to the PyPassword Generator!')
how_many_letters = int(input('How many letters would you like in your password?\n'))
how_many_symbols = int(input('How many symbols would you like?\n'))
how_many_numbers = int(input('How many numbers would you like?\n'))

password = []
for l in range(how_many_letters):
    password.append(random.choice(letters))
for s in range(how_many_symbols):
    password.append(random.choice(symbols))    
for n in range(how_many_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
random_pass = ''
for char in password:
    random_pass += char
print(random_pass)
