# Reproduce the Bug
"""list have indexes which start with zero, not with one
so when variable 'dice_imgs' have index '6' - code will show error 'IndexError: list index out of range'"""
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# it must be like - dice_num = randint(0, 5)
dice_num = randint(1, 6)
# for unlimited bug we must change next string on - print(dice_imgs[6])
print(dice_imgs[dice_num])
