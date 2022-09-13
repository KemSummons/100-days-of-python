import random
from art import logo
import os

intro = input('Do you want to play blackjack? Type "y" for play or "n" for exit. ')
if intro == 'n':
    exit()


def blackjack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_card_1 = random.choice(cards)
    player_card_2 = random.choice(cards)
    player_points = player_card_1 + player_card_2
    dealer_card_1 = random.choice(cards)
    dealer_card_2 = random.choice(cards)
    dealer_points = dealer_card_1 + dealer_card_2

    print(f'Player cards are: [{player_card_1}, {player_card_2}] - {player_points} points')
    print(f'Dealer cards are: [{dealer_card_1}, *]')

    game = True
    while game:
        another_card = input('Do you want one more card? Type "y" or "n": ')
        if another_card == 'y':
            player_another_card = random.choice(cards)
            player_points += player_another_card
            print(f'Player cards are: [{player_card_1}, {player_card_2}, {player_another_card}] - {player_points} points')
            print(f'Dealer cards are: [{dealer_card_1}, *]')
        else:
            print(f'Player cards are: [{player_card_1}, {player_card_2}] - {player_points} points')
            print(f'Dealer cards are: [{dealer_card_1}, {dealer_card_2}] - {dealer_points} points')
            if int(player_points) < int(dealer_points):
                print('You lose!')
                one_more_game = input('Do you want to play more? Type "y" for play or "n" for exit. ')
                if one_more_game == 'n':
                    exit()
                else:
                    os.system('cls')
                    blackjack()
            elif int(player_points) > int(dealer_points):
                print('You win!')
                print(input('Do you want to play more? Type "y" for play or "n" for exit. '))
                one_more_game = input('Do you want to play more? Type "y" for play or "n" for exit. ')
                if one_more_game == 'n':
                    exit()
                else:
                    os.system('cls')
                    blackjack()
            else:
                print('Draw!')
                print(input('Do you want to play more? Type "y" for play or "n" for exit. '))
                one_more_game = input('Do you want to play more? Type "y" for play or "n" for exit. ')
                if one_more_game == 'n':
                    exit()
                else:
                    os.system('cls')
                    blackjack()


blackjack()
