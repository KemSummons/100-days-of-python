from finding_color_list import color_list
from turtle import *
import random
colormode(255)

timmy = Turtle(shape='turtle')
timmy.speed(5)
y_shift = 0


def one_step():
    timmy.color(random.choice(color_list))
    timmy.pendown()
    timmy.dot(20)
    timmy.penup()
    timmy.forward(50)
    global steps
    steps -= 1


def one_row():
    timmy.hideturtle()
    timmy.penup()
    timmy.setx(-200)
    timmy.showturtle()
    for i in range(10):
        one_step()
    timmy.hideturtle()
    timmy.home()
    timmy.sety(y_shift)
    timmy.showturtle()


steps = 30
while steps > 0:
    for row in range(5):
        y_shift += 50
        one_row()

    timmy.hideturtle()

screen = Screen()
screen.exitonclick()
