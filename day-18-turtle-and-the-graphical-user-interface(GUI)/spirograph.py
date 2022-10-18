from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.speed('fastest')
colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.color(r, g, b)


def times_of_spins(times):
    for _ in range(int(360 / times)):
        timmy.circle(100)
        timmy.left(times)
        change_color()


times_of_spins(7)

timmy_screen = Screen()
timmy_screen.exitonclick()
