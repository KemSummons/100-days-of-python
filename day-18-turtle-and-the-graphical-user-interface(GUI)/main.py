from finding_color_list import color_list
from turtle import *
import random
colormode(255)

timmy = Turtle(shape='turtle')
timmy.speed(0.6)


def row():
    timmy.color(random.choice(color_list))
    timmy.pendown()
    timmy.dot(20)
    timmy.penup()
    timmy.forward(50)
    global steps
    steps -= 1


steps = 50
while steps > 0:
    timmy.setx(-200)
    for i in range(10):
        row()
    timmy.penup()
    timmy.hideturtle()
    timmy.home()
    timmy.showturtle()


screen = Screen()
screen.exitonclick()