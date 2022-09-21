# Play Computer
year = int(input("What's your year of birth?"))
# if input number lower 1981 - program print nothing
# if input is 1994 - program print nothing
if year > 1980 and year < 1994:
    print("You are a millenial.")
# for debugging next string must be like a - elif year >= 1994:
elif year > 1994:
    print("You are a Gen Z.")
