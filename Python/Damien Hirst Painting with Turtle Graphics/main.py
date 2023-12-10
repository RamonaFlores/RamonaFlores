import random
import turtle
from random import *
from turtle import Turtle

timmy = Turtle()
timmy.shape("turtle")
timmy.color("light blue")
color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', "light blue", "light green", "pink"]
directions = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed("fastest")


def angela_random_walk(times):
    for _ in range(times):
        timmy.color(color_list[randint(0, len(color_list)-1)])
        timmy.forward(30)
        timmy.setheading(directions[randint(0, len(directions)-1)])


def draw_shape(num_sides):
    color_n = randint(0, len(color_list) - 1)
    timmy.color(color_list[color_n])
    angle = 360 / num_sides
    for i in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


def random_walk():
    color_n = randint(0, len(color_list) - 1)
    timmy.color(color_list[color_n])
    random_x = randint(0, 1)
    print(random_x)
    if random_x == 0:
        timmy.right(90)
        timmy.forward(50)
    else:
        timmy.left(90)
        timmy.forward(50)


angela_random_walk(30)
screen = turtle.Screen()
screen.exitonclick()
