height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
round_bmi = round(weight / height ** 2)
if round_bmi < 18.5:
    print(f'Your BMI is {round_bmi}, you are underweight.')
elif round_bmi < 25:
    print(f'Your BMI is {round_bmi}, you have a normal weight.')
elif round_bmi < 30:
    print(f'Your BMI is {round_bmi}, you are slightly overweight.')
elif round_bmi < 35:
    print(f'Your BMI is {round_bmi}, you are obese.')
else:
    print(f'Your BMI is {round_bmi}, you are clinically obese.')
