from menu_of_coffee import *
money = 0


def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney: ${money}'


def kinds_of_coffee():
    wish = input('What would you like? (espresso/latte/cappuccino): ')
    if wish == 'off':
        exit()
    elif wish == 'report':
        print(report())
    elif wish == 'espresso':
        return 'espresso'
    elif wish == 'latte':
        return 'latte'
    elif wish == 'cappuccino':
        return 'cappuccino'
    else:
        print('Invalid enter. Try again.')
        while wish != 'off' or wish != 'report' or wish != 'espresso' or wish != 'latte' or wish != 'cappuccino':
            return kinds_of_coffee()


# if kinds_of_coffee() == 'espresso' or kinds_of_coffee() == 'latte' or kinds_of_coffee() == 'cappuccino':
def check_resources(resources, coffee_type):
    if resources['water'] > MENU[f'{coffee_type}']['ingredients']['water']:
        return True
    if resources['milk'] > MENU[f'{coffee_type}']['ingredients']['milk']:
        return True
    if resources['coffee'] > MENU[f'{coffee_type}']['ingredients']['coffee']:
        return True
    else:
        return False


print(check_resources(resources, kinds_of_coffee()))


# coffee_machine_on = True
# while coffee_machine_on:
#     kinds_of_coffee()
#     check_resources(resources, kinds_of_coffee())
#     # if check_resources():
#     print(check_resources(resources, kinds_of_coffee()))
