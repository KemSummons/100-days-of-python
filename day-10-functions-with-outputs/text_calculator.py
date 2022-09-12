from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operations_symbol = input('Pick an operation from the line above: ')
    num2 = float(input("What's the second number?: "))
    first_answer = round(operations[operations_symbol](num1, num2), 3)
    print(f'{num1} {operations_symbol} {num2} = {first_answer}')
    second_answer = first_answer
    infinity_calculations = True
    while infinity_calculations:
        more_operations = input(
            f'Type "exit" for out from program.\nType "yes" for use another operations with {second_answer} or "no" to start a new calculation:  ')
        if more_operations == 'exit':
            infinity_calculations = False
            print('Goodbye!')
        elif more_operations == 'no':
            calculator()
        elif more_operations == 'yes':
            operations_symbol = input("Pick an operation ('+', '-', '*', '/'): ")
            next_num = float(input("What's the next number?: "))
            second_answer = round(operations[operations_symbol](second_answer, next_num), 3)
            print(f'{first_answer} {operations_symbol} {next_num} = {second_answer}')
        else:
            print('Invalid enter!')


calculator()
