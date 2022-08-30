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

word_list = ["aardvark", "baboon", "camel", "raccoon"]
chosen_word = random.choice(word_list)
lives = 6

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
    if guess not in chosen_word:
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