import random
from hangman_arts import *
from hangman_words import *

chosen_word = random.choice(word_list)
lives = 6

print(logo)
display = []
for letter in chosen_word:
    display += "_"
print(display)

while "_" in display:
    guess = input('Guess a letter: ').lower()

    if guess in display:
        print(f'You already guessed "{guess}".')
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        if guess not in display:
            print(f'Word dont have "{guess}". You losses life.')
        lives -= 1
        if lives == 0:
            print(stages[0])
            print('You lose!')
            break
    print(f"{' '.join(display)}")
    if "_" not in display:
        print('You win!')
        break
    print(stages[lives])
