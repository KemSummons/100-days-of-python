import string
from art import *

print(logo)
alphabet = list(string.ascii_lowercase)
direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
while direction != 'encode' and direction != 'decode':
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
text = input('Type your message:\n').lower()
shift = int(input('Type the shift number:\n'))


def caesar(text, shift, direction):
    final_text = ''
    if direction == 'decode':
        shift *= -1
    for letter in text:
        index_letter = alphabet.index(letter)
        shift_index_letter = (index_letter + shift) % 26
        cipher_letter = alphabet[shift_index_letter]
        final_text += cipher_letter
    print(f'The {direction} text is "{final_text}".')


caesar(text, shift, direction)
