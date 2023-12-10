import turtle
from random import *
from turtle import Turtle
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("light blue")

directions = [0, 90, 180, 270]
timmy.pensize(1)
timmy.speed("fastest")
turtle.colormode(255)


def spirograph(times):
    heading = 0
    for _ in range(times):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(heading)
        heading+=10


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def angela_random_walk(times):
    for _ in range(times):
        timmy.color(random_color())
        timmy.forward(30)
        timmy.setheading(directions[randint(0, len(directions) - 1)])


spirograph(100)
screen = turtle.Screen()
screen.exitonclick()
