import os
import random
from art import *
from game_data import data


def random_account():
    return random.choice(data)


def info(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_description}, from {account_country}.'


def answer(guess, a_followers, b_followers):
    if guess == 'a':
        if a_followers > b_followers:
            return True
        else:
            return False
    else:
        if a_followers < b_followers:
            return True
        else:
            return False


def game():
    print(logo)
    score = 0
    game_on = True
    account_a = random_account()
    account_b = random_account()

    while game_on:
        account_a = account_b
        account_b = random_account()

        while account_a == account_b:
            account_b = random_account()

        print(f"Side A: {info(account_a)}")
        print(vs)
        print(f"Side B: {info(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers_count = account_a['follower_count']
        b_followers_count = account_b['follower_count']
        is_correct = answer(guess, a_followers_count, b_followers_count)

        os.system('cls')
        print(logo)
        if is_correct:
            score += 1
            print(f'You are right! Score now is: "{score}".')
        else:
            game_on = False
            print(f'You are now right! Final score: "{score}".')


game()
