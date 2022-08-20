import random

rock = '''
    _______
---'     ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''

paper = '''
    _______
---'     ____)____
              ______)
              _______)
            _______)
---.__________)
'''

scissors = '''
    _______
---'     ____)____
              ______)
         __________)
        (____)
---.__(___)
'''


player_choice = int(input("Enter '1' for rock, '2' for paper, '3' for scissors."))
if player_choice == 1:
    print(rock)
elif player_choice == 2:
    print(paper)
elif player_choice == 3:
    print(scissors)

random_digit = random.randint(1, 3)
if random_digit == 1:
    print(rock)
elif random_digit == 2:
    print(paper)
else:
    print(scissors)

if player_choice == 1 and random_digit == 1:
    print('Draw!')
elif player_choice == 1 and random_digit == 2:
    print('You lose!')
elif player_choice == 1 and random_digit == 3:
    print('You win!')
elif player_choice == 2 and random_digit == 1:
    print('You win!')
elif player_choice == 2 and random_digit == 2:
    print('Draw!')
elif player_choice == 2 and random_digit == 3:
    print('You lose!')
elif player_choice == 3 and random_digit == 1:
    print('You lose!')
elif player_choice == 3 and random_digit == 2:
    print('You win!')
elif player_choice == 3 and random_digit == 3:
    print('Draw!')
else:
    print('You tap invalid command!')