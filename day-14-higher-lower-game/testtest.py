import os
import random
from art import *
from game_data import data

random_first = random.choice(data)
random_second = random.choice(data)
while random_second == random_first:
    random_second = random.choice(data)


def first_side():
    winner = f"Side A: {random_first['name']}, a {random_first['description']}, from {random_first['country']}"
    return winner


def second_side():
    challenger = f"Side B: {random_second['name']}, a {random_second['description']}, from {random_second['country']}"
    return challenger


def confrontation():
    count = 0
    print(logo)
    print(first_side())
    print(vs)
    print(second_side())
    question = input("Who has more followers? Type 'A' or 'B': ").lower()
    if question == 'a':
        if random_first['follower_count'] > random_second['follower_count']:
            count += 1
            print(f'You are right! Your score now is: "{count}".')
        else:
            os.system('cls')
            print(f'You are not right! Final score: "{count}".')
            exit()
    elif question == 'b':
        if random_first['follower_count'] < random_second['follower_count']:
            count += 1
            print(f'You are right! Your score now is: "{count}".')
        else:
            os.system('cls')
            print(f'You are not right! Final score: "{count}".')
            exit()
    else:
        print(f'Invalid enter! Final score: {count}')


confrontation()

game_on = True
while game_on:
    confrontation()
