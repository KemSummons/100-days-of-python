from finding_color_list import color_list
from turtle import *
import random
colormode(255)

timmy = Turtle(shape='turtle')
timmy.speed('fastest')
y_shift = 0
timmy.penup()


def one_step():
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)


def one_row():
    timmy.hideturtle()
    timmy.setx(-200)
    timmy.showturtle()
    for i in range(10):
        one_step()
    timmy.hideturtle()
    timmy.home()
    timmy.sety(y_shift)
    timmy.showturtle()


steps = 5
while steps > 0:
    for row in range(5):
        y_shift += 50
        one_row()
        steps -= 1
        if steps <= 0:
            break
    timmy.hideturtle()

screen = Screen()
screen.exitonclick()
