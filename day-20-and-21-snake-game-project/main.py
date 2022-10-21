from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
x_position = [0, -20, -40]


for part_of_snake in range(0, len(x_position)):
    new_part = Turtle(shape='square')
    new_part.color('white')
    new_part.penup()
    new_part.goto(x_position[part_of_snake], 0)
















screen.exitonclick()
