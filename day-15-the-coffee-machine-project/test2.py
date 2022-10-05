from menu_of_coffee import *
import os


def kinds_of_coffee():
    wish = input('What would you like? (espresso - $1.5/latte - $2.5/cappuccino - $3): ')
    return wish


def check_resources(res, coffee_type):
    if res['water'] > MENU[f'{coffee_type}']['ingredients']['water']:
        return True
    if res['milk'] > MENU[f'{coffee_type}']['ingredients']['milk']:
        return True
    if res['coffee'] > MENU[f'{coffee_type}']['ingredients']['coffee']:
        return True
    else:
        return False


def input_money(coffee_type):
    print('Please insert coins.')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))
    sum_of_coins = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if sum_of_coins > MENU[f'{coffee_type}']['cost']:
        remains = round(sum_of_coins - MENU[f'{coffee_type}']['cost'], 2)
        print(f'Here is ${remains} in change.\nHere is your {coffee_type} ☕. Enjoy!')
        kinds_of_coffee()
    else:
        print("Sorry that's not enough money. Money refunded.")
        kinds_of_coffee()


print(input_money(kinds_of_coffee()))

money = 0
coffee_machine_on = True
while coffee_machine_on:
    kinds_of_coffee()
    if kinds_of_coffee() == 'off':
        exit()
    elif kinds_of_coffee() == 'report':
        def report():
            water = resources['water']
            milk = resources['milk']
            coffee = resources['coffee']
            return f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney: ${money}'
    check_resources(resources, coffee_type=kinds_of_coffee())
    if check_resources(resources, coffee_type=kinds_of_coffee()):
        input_money(coffee_type=kinds_of_coffee())
        os.system('cls')
