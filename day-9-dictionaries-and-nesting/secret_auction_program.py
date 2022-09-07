from art import logo

print(logo)
print('Welcome to the secret auction!')

player_list = []
continuation_of_auction = True
while continuation_of_auction:
    player_name = input('What is your name?\n')
    player_bet = float(input('What is your bet?\n$ '))

    dictionary_of_betting = {}
    dictionary_of_betting[player_name] = player_bet
    player_list.append(dictionary_of_betting)

    another_player = input('Are there any other players? Type "yes" or "no".\n').lower()
    if another_player == 'no':
        continuation_of_auction = False

len_of_player_list = len(player_list)
for elem in range(1, len_of_player_list):
    player_list[0].update(player_list[elem])

print(player_list[0])


for player in player_list[0]:
    bet = 0
    if player_list[0][player] > bet:
        bet = player_list[0][player]
print(f'Winner is with bet $ {bet}!')
