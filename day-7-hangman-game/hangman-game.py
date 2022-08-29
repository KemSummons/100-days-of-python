import random
stages = ['''
  +---+  
  |     |
  O    |
 /|\    |
 / \    |
         |
=========
''', '''
  +---+
  |     |
  O    |
 /|\    |
 /      |
        |
=========
''', '''
  +---+
  |     |
  O    |
 /|\   |
        |
        |
=========
''', '''
  +---+
  |     |
  O    |
 /|     |
        |
        |
=========''', '''
  +---+
  |     |
  O    |
  |     |
        |
        |
=========
''', '''
  +---+
  |     |
  O    |
        |
        |
        |
=========
''', '''
  +---+
   |    |
        |
        |
        |
        |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display += "_"
print(display)

while "_" in display:
    guess = input('Guess a letter: ').lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
print('You win!')
