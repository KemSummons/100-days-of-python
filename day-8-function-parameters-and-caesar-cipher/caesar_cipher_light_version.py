import string

alphabet = list(string.ascii_lowercase)
direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
while direction != 'encode' and direction != 'decode':
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
text = input('Type your message:\n').lower()
shift = int(input('Type the shift number:\n'))

def caesar(text, shift, direction):
    final_text = ''
    for letter in text:
        index_letter = alphabet.index(letter)
        if direction == 'encode':
            shift_index_letter = (index_letter + shift) % 26
            cipher_letter = alphabet[shift_index_letter]
            final_text += cipher_letter
        else:
            shift_index_letter = (index_letter - shift) % 26
            original_letter = alphabet[shift_index_letter]
            final_text += original_letter
    print(f'The {direction} text is "{final_text}".')


caesar(text, shift, direction)
