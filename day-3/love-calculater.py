print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1_lower = name1.lower()
name2_lower = name2.lower()
names_lower = name1_lower + name2_lower
names_lower_t = names_lower.count('t')
names_lower_r = names_lower.count('r')
names_lower_u = names_lower.count('u')
names_lower_e = names_lower.count('e')
names_lower_l = names_lower.count('l')
names_lower_o = names_lower.count('o')
names_lower_v = names_lower.count('v')
names_lower_e2 = names_lower.count('e')
count_true = names_lower_t + names_lower_r + names_lower_u + names_lower_e
count_love = names_lower_l + names_lower_o + names_lower_v + names_lower_e2
count_result = int(str(count_true) + str(count_love))
if count_result < 10 or count_result > 90:
    print(f'Your score is {count_result}, you go together like coke and mentos.')
elif 40 <= count_result <= 50:
    print(f'Your score is {count_result}, you are alright together.')
else:
    print(f'Your score is {count_result}.')
