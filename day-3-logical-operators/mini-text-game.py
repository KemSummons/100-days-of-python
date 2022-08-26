print("Welcome to the 'Try to survive!'")
print("You is wake up in full white room. You see 2 doors, on front and on back.")
step_1 = input("Choose 'front' or 'back' to continuum.").lower()
if step_1 == 'front':
    print('You open front door and come to room with zombie')
    print("You see three zombies, first with big foots, second with long hands and third with one eye.")
    zombie = input("Which zombie less dangerous from your opinion? You choose zombie with 'foots', 'hands' or 'eye'?").lower()
    if zombie == 'hands':
        print('You choose zombie with long hands, trying to running past, but zombie grab you his long hands and devour you.')
        print('Game over! You was devoured!')
    elif zombie == 'foots':
        print('You choose zombie with big foots, trying to running past, but zombie jump on you and crush you into a flat cake.')
        print('Game over! You was squashed!')
    elif zombie == 'eye':
        print('You choose zombie with one eye, trying to running past, zombie just look on you and do nothing.')
        print('You go out from room with zombies and come to table with cups.')
        liquid = input("On table stay 3 cups with liquid: 'black', 'red' and 'blue'. What you choose?").lower()
        if liquid == 'black':
            print('You choose black liquid, it was poison.')
            print('Game over! You was poisoned!')
        elif liquid == 'red':
            print('You choose red liquid, it was blood. After drunk blood you transform in vampire.')
            print('Game over! You lived 1000 years like a monster!')
        elif liquid == 'blue':
            print('You choose blue liquid, it was water of life.')
            print('With new body and skills you survived! Congratulations!')
        else:
            print("Game over! You couldn't make a choice and died of doubts!")
    else:
        print('You wait so much and zombies devour you.')
        print('Game over! You was devoured!')
elif step_1 == 'back':
    print('You open back door and come to room with cats')
    print('Cats attack you they soft paws.')
    print('Game over! You died from cuteness!')
else:
    print('You wait so much and starve to death')
