import random
from art import logo
import os


def intro():
    intro = input('Do you want to play blackjack? Type "y" for play or "n" for exit. ')
    if intro == 'y':
        os.system('cls')
        blackjack()
    else:
        exit()


def blackjack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_card_1 = random.choice(cards)
    player_card_2 = random.choice(cards)
    player_list = []
    player_list.append(player_card_1), player_list.append(player_card_2)
    player_total = 0
    for elem in range(len(player_list)):
        player_total += player_list[elem]
    dealer_card_1 = random.choice(cards)
    dealer_card_2 = random.choice(cards)
    dealer_list = []
    dealer_list.append(dealer_card_1), dealer_list.append(dealer_card_2)
    dealer_total = 0
    for elem in range(len(dealer_list)):
        dealer_total += dealer_list[elem]
    print(f'Player cards are: {player_list} - {player_total} points')
    print(f'Dealer cards are: [{dealer_card_1}, *]')

    game = True
    while game:
        another_card = input('Do you want one more card? Type "y" or "n": ')
        if another_card == 'y':
            player_another_card = random.choice(cards)
            player_list.append(player_another_card)
            player_total += player_another_card
            print(f'Player cards are: {player_list} - {player_total} points')
            print(f'Dealer cards are: [{dealer_card_1}, *]')
            if player_total > 21 and dealer_total <= 21:
                print('You have over much points! You lose!')
                intro()
        else:
            while dealer_total < 17:
                dealer_another_card = random.choice(cards)
                dealer_list.append(dealer_another_card)
                dealer_total += dealer_another_card
            print(f'Player cards are: {player_list} - {player_total} points')
            print(f'Dealer cards are: {dealer_list} - {dealer_total} points')
            if dealer_total > 21:
                print('You win!')
                intro()
            elif player_total < dealer_total:
                print('You lose!')
                intro()
            elif player_total > dealer_total:
                print('You win!')
                intro()
            else:
                print('Draw!')
                intro()


intro()
