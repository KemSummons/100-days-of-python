from turtle import Turtle, Screen

tim = Turtle(shape='turtle')


def up():
    tim.setheading(90)


def down():
    tim.setheading(270)


def left():
    tim.setheading(180)


def right():
    tim.setheading(0)


screen = Screen()
screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')
screen.exitonclick()
