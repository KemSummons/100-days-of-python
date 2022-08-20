import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
score_in_list = len(names)
number_of_payer = random.randint(0, (score_in_list - 1))
payer = names[number_of_payer]
print(f'{payer} was chosen!')
