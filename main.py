
import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

colors = ["red", "green", "blue", "orange", "purple", "yellow", "violet", "gray"]

for line in range(3, 11):
    angle = 360 / int(line)
    random_color = random.choice(colors)
    tim.pencolor(random_color)

    for shape in range(line):
        tim.forward(100)
        tim.left(angle)

screen.exitonclick()
