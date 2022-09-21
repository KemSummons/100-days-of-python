# Describe Problem
"""'for-loop' check all elements between 1 and 20, without 20
when element == 20, function print 'You got it'
bug here - if we use 'for in range' - we don't take last digit, so for debugging we must switch 20 on 21"""
def my_function():
    # it must be like - for i in range(1, 21):
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()
