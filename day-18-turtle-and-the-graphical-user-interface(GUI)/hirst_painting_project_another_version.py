from finding_color_list import color_list
from turtle import *
import random
colormode(255)

timmy = Turtle(shape='turtle')
timmy.speed('fastest')
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
steps = 50

for steps_count in range(1, steps + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if steps_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()
