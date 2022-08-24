import string
import random
letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# some symbols can don't work in password, so we will use limited list, in another situation we will use list(string.punctuation)

print("Welcome to the Password Generator!")
amount_of_letters = int(input("How many letters would you like in your password?\n"))
amount_of_numbers = int(input(f"How many symbols would you like in your password?\n"))
amount_of_symbols = int(input(f"How many numbers would you like in your password?\n"))

# easy mode № 1 with characters in order
random_letter = random.choices(letters, k=amount_of_letters)
random_number = random.choices(numbers, k=amount_of_numbers)
random_symbols = random.choices(symbols, k=amount_of_symbols)
letters_in_password = ''.join(map(str, random_letter))
letters_in_number = ''.join(map(str, random_number))
letters_in_symbols = ''.join(map(str, random_symbols))
final_password = letters_in_password + letters_in_number + letters_in_symbols
print(final_password)

# harder mode № 1 with characters not in order
mixed_final_password = ''.join(random.sample(final_password, len(final_password)))
print(mixed_final_password)

# easy mode № 2 with characters in order
password = ''
for character in range(1, amount_of_letters + 1):
    password += random.choice(letters)
for character in range(1, amount_of_numbers + 1):
    password += random.choice(numbers)
for character in range(1, amount_of_symbols + 1):
    password += random.choice(symbols)
print(password)

# harder mode № 2 with characters not in order
list_password = list(password)
random.shuffle(list_password)
our_password = ''.join(list_password)
print(our_password)
