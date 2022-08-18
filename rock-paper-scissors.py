import random

player_choice = int(input("Enter '1' for rock, '2' for paper, '3' for scissors."))
if player_choice == 1:
    print('Rock')
elif player_choice == 2:
    print('Paper')
elif player_choice == 3:
    print('Scissors')

random_digit = random.randint(1, 3)
if random_digit == 1:
    print('Rock')
elif random_digit == 2:
    print('Paper')
else:
    print('Scissors')

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
else:
    print('Draw!')