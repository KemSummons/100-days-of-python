from turtle import *
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.speed(500)
timmy.pensize(10)
colormode(255)


def change_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    timmy.color(R, G, B)

# or:
# def change_color():
#     R = random.random()
#     G = random.random()
#     B = random.random()
#     timmy.color(R, G, B)


list_direction = [0, 90, 180, 270]

steps = 500
while steps >= 0:
    timmy.fd(30)
    timmy.setheading(random.choice(list_direction))
    change_color()
    steps -= 1

# or:
# for _ in range(300):
#     timmy.fd(30)
#     timmy.setheading(random.choice(list_direction))
#     change_color()


timmy_screen = Screen()
timmy_screen.exitonclick()
