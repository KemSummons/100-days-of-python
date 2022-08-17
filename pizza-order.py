print("Welcome to Python Pizza Deliveries!")
size = (input("What size pizza do you want? S, M, or L ")).upper()
add_pepperoni = (input("Do you want pepperoni? Y or N ")).upper()
extra_cheese = (input("Do you want extra cheese? Y or N ")).upper()

bill = 0
if size == 'S':
    if add_pepperoni == 'Y':
        bill = 17
    else:
        bill = 15
elif size == 'M':
    if add_pepperoni == 'Y':
        bill = 23
    else:
        bill = 20
else:
    if add_pepperoni == 'Y':
        bill = 28
    else:
        bill = 25

if extra_cheese == 'Y':
    bill += 1

print(f'Your final bill is: ${bill}.')
