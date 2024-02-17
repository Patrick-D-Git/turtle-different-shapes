
import random
from turtle import Turtle, Screen

tim = Turtle()  # Turtle class
screen = Screen()  # Screen class

colors = ["red", "green", "blue", "orange", "purple", "yellow", "violet", "gray"]


def draw_shape(n_sides):
    """"""
    angle = 360 / int(n_sides)
    for _ in range(n_sides):
        tim.forward(100)
        tim.left(angle)


for lines in range(3, 11):
    random_color = random.choice(colors)
    tim.pencolor(random_color)
    draw_shape(lines)


screen.exitonclick()  # Shows the white box
