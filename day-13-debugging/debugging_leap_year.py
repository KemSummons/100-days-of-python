# in 4 string we have bug - input have 'string' type
# for if-else construction on 5-14 strings used integers
# so we must adding before input int() like a - year = int(input("Which year do you want to check?"))
year = input("Which year do you want to check?")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
