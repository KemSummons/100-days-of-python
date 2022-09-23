import os
import random
from art import *
from game_data import data

random_first = random.choice(data)
random_second = random.choice(data)
print(logo)
first_side = f"Side A: {random_first['name']}, a {random_first['description']}, from {random_first['country']}"
print(first_side)
print(vs)
second_side = f"Side B: {random_second['name']}, a {random_second['description']}, from {random_second['country']}"
print(second_side)
question = input("Who has more followers? Type 'A' or 'B': ").lower()


def game():
    count = 0
    if question == 'a':
        if random_first['follower_count'] > random_second['follower_count']:
            print('You are right!')
            count += 1
            print(count)
        else:
            os.system('cls')
            print('You are not right!')
            exit()
    elif question == 'b':
        if random_first['follower_count'] < random_second['follower_count']:
            print('You are right!')
            count += 1
            print(count)
        else:
            os.system('cls')
            print('You are not right!')
            exit()
    else:
        print(f'Invalid enter! Final score: {count}')


game()
