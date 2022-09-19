import random
from art import logo
import os


def another_game():
    one_more_game = input('Do you want play more? Type "y" or "n": ')
    if one_more_game == 'y':
        os.system('cls')
        start_game()
    else:
        print('Goodbye!')
        exit()


def start_game():
    print(logo)
    print('Welcome to the "Number Guessing Game"!\nYou must guess a digit between 1 and 100!')
    difficult = input('Choose difficulty of the game. Type "easy" or "hard". ')
    lives = 0
    if difficult == 'easy':
        print('You choose easy game. You have "10" lives - attempts to guess the hidden number.')
        lives = 10
    elif difficult == 'hard':
        print('You choose hard game. You have "5" lives - attempts to guess the hidden number.')
        lives = 5
    else:
        os.system('cls')
        start_game()

    digit = random.randint(1, 100)
    game_continue = True
    while game_continue:
        guess = int(input('Choose the digit: '))
        if lives == 0:
            game_continue = False
            print(f'You lose all lives. The guessed number was "{digit}".')
            another_game()
        elif guess < digit:
            lives -= 1
            print(f"Too low. You lose a live. Remaining lives - {lives}.")
        elif guess > digit:
            lives -= 1
            print(f"Too high. You lose a live. Remaining lives - {lives}.")
        else:
            print(f'You are right! The guessed number was "{digit}".')
            another_game()


start_game()
