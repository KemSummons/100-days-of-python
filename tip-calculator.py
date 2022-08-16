print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill?\n$'))
total_tip = int(input('What percentage tip would you like to give? 10, 12 or 15?\n'))
total_people = int(input('How many people to split the bill?\n'))
value_percentage = total_bill * total_tip / 100
result = (total_bill + value_percentage) / total_people
round_result = round(result, 2)
print(f"Each person should pay: $ {format(result, '.2f')}")
