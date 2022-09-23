import os
import random
from art import *
from game_data import data


random_first = random.choice(data)
random_second = random.choice(data)
while random_second == random_first:
    random_second = random.choice(data)
# question = input("Who has more followers? Type 'A' or 'B': ").lower()


def first_side(name, description, country):
    followers = random_first['follower_count']
    print(followers)
    return f"Side A: {random_first['name']}, a {random_first['description']}, from {random_first['country']}"


def second_side(name, description, country):
    followers = random_second['follower_count']
    print(followers)
    return f"Side A: {random_second['name']}, a {random_second['description']}, from {random_second['country']}"


side_a = first_side(name=random_first['name'], description=random_first['description'], country=random_first['country'])
side_b = second_side(name=random_second['name'], description=random_second['description'], country=random_second['country'])


def versus(side_a, side_b):
    print(logo)