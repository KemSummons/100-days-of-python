from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)


def one_step(num_sides):
    angle = 360 / num_sides
    for side in range(num_sides):
        timmy.forward(100)
        timmy.left(angle)


for shape_side_n in range(3, 11):
    one_step(shape_side_n)
    change_color()


timmy_screen = Screen()
timmy_screen.exitonclick()
