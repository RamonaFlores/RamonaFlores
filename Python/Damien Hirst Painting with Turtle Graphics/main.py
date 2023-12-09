import turtle
from turtle import Turtle

timmy = Turtle()
timmy.shape("turtle")
timmy.color("light blue")
for n in range(0, 4):
    timmy.forward(100)
    timmy.left(90)

screen = turtle.Screen()
screen.exitonclick()
