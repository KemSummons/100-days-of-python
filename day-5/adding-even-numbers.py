digit = 0
for number in range(2, 101, 2):
    digit += number
print(digit)

# we can use this method too:
digit = 0
for number in range(1, 101):
    if number % 2 == 0:
        digit += number
print(digit)
