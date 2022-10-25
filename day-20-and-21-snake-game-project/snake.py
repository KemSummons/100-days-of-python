from turtle import Turtle
STARTING_X_POSITION = [0, -20, -40]
MOVE_DISTANCE = 20
turtle = Turtle()


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()

    def create_snake(self):
        for part_of_snake in range(0, len(STARTING_X_POSITION)):
            new_part = Turtle(shape='square')
            new_part.color('white')
            new_part.penup()
            new_part.goto(STARTING_X_POSITION[part_of_snake], 0)
            self.snake_list.append(new_part)

    def move(self):
        for list_elem in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[list_elem - 1].xcor()
            new_y = self.snake_list[list_elem - 1].ycor()
            self.snake_list[list_elem].goto(new_x, new_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    def up(self):
        turtle.setheading(90)

    def down(self):
        turtle.setheading(90)

    def left(self):
        turtle.setheading(90)

    def right(self):
        turtle.setheading(90)
