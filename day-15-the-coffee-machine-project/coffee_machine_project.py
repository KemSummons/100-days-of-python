from menu_of_coffee import *
money = 0


def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney: ${money}'


def kinds_of_coffee():
    wish = input('What would you like? (espresso - $1.5/latte - $2.5/cappuccino - $3): ')
    if wish == 'off':
        exit()
    # elif wish == 'report':
    #     return report()
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


#if kinds_of_coffee() == 'espresso' or kinds_of_coffee() == 'latte' or kinds_of_coffee() == 'cappuccino':
def check_resources(resources, coffee_type):
    if resources['water'] > MENU[f'{coffee_type}']['ingredients']['water']:
        return True
    if resources['milk'] > MENU[f'{coffee_type}']['ingredients']['milk']:
        return True
    if resources['coffee'] > MENU[f'{coffee_type}']['ingredients']['coffee']:
        return True
    else:
        return False


required_resources = check_resources(resources, kinds_of_coffee())
print(required_resources)


def finished_coffee(resources, coffee_type):
    if required_resources:
        resources['water'] -= MENU[f'{coffee_type}']['ingredients']['water']
        resources['milk'] -= MENU[f'{coffee_type}']['ingredients']['milk']
        resources['coffee'] -= MENU[f'{coffee_type}']['ingredients']['coffee']

        return



# coffee_machine_on = True
# while coffee_machine_on:
#     kinds_of_coffee()
#     check_resources(resources, kinds_of_coffee())
#     # if check_resources():
#     print(check_resources(resources, kinds_of_coffee()))
