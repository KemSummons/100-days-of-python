import string

alphabet = list(string.ascii_lowercase)
direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
text = input('Type your message:\n').lower()
shift = int(input('Type the shift number:\n'))


def encrypt(text, shift):
    cipher_text_list = []
    for x in text:
        index = alphabet.index(x)
        shift_index = index + shift
        if shift_index < len(alphabet):
            cipher_letter = alphabet[shift_index]
            cipher_text_list += cipher_letter
        else:
            shift_index = shift_index % 26
            cipher_letter = alphabet[shift_index]
            cipher_text_list += cipher_letter
    cipher_text = ''.join(cipher_text_list)
    print(f'The encoded text is "{cipher_text}".')


def decrypt(text, shift):
    original_text_list = []
    for x in text:
        index = alphabet.index(x)
        shift_index = index - shift
        original_letter = alphabet[shift_index]
        original_text_list += original_letter
    original_text = ''.join(original_text_list)
    print(f'The decoded text is "{original_text}".')


if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)

