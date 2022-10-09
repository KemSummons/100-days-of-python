from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_on = True
while coffee_machine_on:
    options = menu.get_items()
    wish = input(f'What would you like? ({options}): ')
    if wish == 'off':
        coffee_machine_on = False
    elif wish == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(wish)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
