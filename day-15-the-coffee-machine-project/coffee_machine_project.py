from menu_of_coffee import *
money = 0


def sufficient_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


def add_coins():
    print("Please insert coins.")
    total = int(input('How many quarters?: ')) - 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        difference = round(money_received - drink_cost, 2)
        print(f'Here is ${difference} in change.')
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


coffee_machine_on = True
while coffee_machine_on:
    wish = input('What would you like? (espresso - $1.5/latte - $2.5/cappuccino - $3): ')
    if wish == 'off':
        coffee_machine_on = False
    elif wish == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[wish]
        if sufficient_resources(drink["ingredients"]):
            payment = add_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(wish, drink["ingredients"])
