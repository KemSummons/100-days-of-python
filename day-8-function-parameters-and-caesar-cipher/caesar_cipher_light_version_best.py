import string
from art import *

alphabet = list(string.ascii_lowercase)


def caesar(text, shift, direction):
    final_text = ''
    if direction == 'decode':
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            final_text += letter
        else:
            index_letter = alphabet.index(letter)
            shift_index_letter = (index_letter + shift) % 26
            cipher_letter = alphabet[shift_index_letter]
            final_text += cipher_letter
    print(f'The {direction} text is "{final_text}".')


print(logo)

continuation = True
while continuation:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))

    caesar(text, shift, direction)

    question = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if question == 'no':
        continuation = False
        print('Goodbye!')
