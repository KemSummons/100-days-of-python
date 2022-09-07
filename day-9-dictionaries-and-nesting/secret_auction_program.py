from art import logo

print(logo)
print('Welcome to the secret auction!')

player_list = []
continuation_of_auction = True
dictionary_of_betting = {}
while continuation_of_auction:
    player_name = input('What is your name?\n')
    player_bet = float(input('What is your bet?\n$ '))

    dictionary_of_betting[player_name] = player_bet
    player_list.append(dictionary_of_betting)

    another_player = input('Are there any other players? Type "yes" or "no".\n').lower()
    if another_player == 'no':
        continuation_of_auction = False

bet = 0
for player in dictionary_of_betting:
    if bet < dictionary_of_betting[player]:
        bet = dictionary_of_betting[player]

name_winner = list(dictionary_of_betting.keys())[list(dictionary_of_betting.values()).index(bet)]
print(f'Winner is {name_winner} with bet $ {bet}!')
