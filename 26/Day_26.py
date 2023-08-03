import pandas

given_name_input = input('Enter the name: ').upper()
given_name_letters = [letter for letter in given_name_input]

df = pandas.read_csv('nato_phonetic_alphabet.csv')
our_dictionary = {row.letter:row.code for (index, row) in df.iterrows()}

print([our_dictionary[word] for word in given_name_letters if word in our_dictionary])