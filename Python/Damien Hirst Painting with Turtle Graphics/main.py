import turtle

from random import *
from turtle import Turtle
import random
import colorgram

timmy = Turtle()
timmy.shape("turtle")
timmy.color("light blue")
timmy.hideturtle()
directions = [0, 90, 180, 270]
timmy.pensize(1)
timmy.speed("fastest")
turtle.colormode(255)
color_tp = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130),
            (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104),
            (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170),
            (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44),
            (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169), (179, 188, 212),
            (48, 74, 73), (147, 37, 35), (43, 62, 61)]
timmy.penup()
timmy.sety(-40)
x = -60
y = -60
timmy.setpos(x, y)
for w in range(10):
    for n in range(10):
        timmy.color(random.choice(color_tp))
        timmy.shape("circle")
        timmy.stamp()
        timmy.forward(50)
        y += 5
    timmy.setpos(x, y)

# def spirograph(size_gap):
#     heading = 0
#     for _ in range(int(360 / size_gap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(heading)
#         heading += size_gap
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# def angela_random_walk(times):
#     for _ in range(times):
#         timmy.color(random_color())
#         timmy.forward(30)
#         timmy.setheading(directions[randint(0, len(directions) - 1)])
#
#
# spirograph(5)
screen = turtle.Screen()
screen.exitonclick()
