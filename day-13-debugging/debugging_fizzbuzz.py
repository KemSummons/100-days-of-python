for number in range(1, 101):
# in string № 4 we have bug - 'FizzBuzz' must printed only if number % 3 == 0 'and' number % 5 == 0, not 'or'
# we must switch 'or' on 'and'
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
# in string № 7 and № 9 we have bug - 'if' must be 'elif' for correct work program
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
# in string № 13 we have bug - no need brackets. it must be like a - print(number)
        print([number])
