from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'\
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_app = True

while continue_app:
    encrypted_word = []
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input('Type your message:\n').lower()
    shift = (int(int(input('Type the shift number:\n')) % 25))

    
    def encrypt(plain_text, shift_amount):
        for letter in plain_text:
            if letter in alphabet:
                the_word_index = alphabet.index(letter)
                encrypted_word.append(alphabet[the_word_index + shift_amount])
            else:
                encrypted_word.append(letter)    
        print(''.join(encrypted_word))

    def decrypt(plain_text, shift_amount):
        for letter in plain_text:
            if letter in alphabet:
                the_word_index = alphabet.index(letter)
                encrypted_word.append(alphabet[the_word_index - shift_amount])
            else:
                encrypted_word.append(letter)
        print(''.join(encrypted_word))


    if direction == 'encode':
        encrypt(text, shift)
        yes_no = input("Do you want to continue? 'yes' or 'no'\n").lower()
        if yes_no == 'yes':
            clear()
        elif yes_no == 'no':
            continue_app = False
        else:
            print("Invalid input. Enter 'yes' or 'no'")
            yes_no = input("Do you want to continue? 'yes' or 'no'\n").lower()

    elif direction == 'decode':
        decrypt(text, shift)
        yes_no = input("Do you want to continue? 'yes' or 'no'\n").lower()
        if yes_no == 'yes':
            clear()
        elif yes_no == 'no':
            continue_app = False
        else:
            print("Invalid input. Enter 'yes' or 'no'")
            yes_no = input("Do you want to continue? 'yes' or 'no'\n").lower()
    else:
        print("Invalid input. Please type 'encode' or 'decode'.")
