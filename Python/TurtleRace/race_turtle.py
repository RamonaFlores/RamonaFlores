from turtle import Turtle


class RaceTurtle:
    def __init__(self, turtle, color, position=0):
        self.turtle = turtle
        self.color = color
        self.turtle.color(self.color)
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.position = position

    def forward_to_line(self, distance):
        self.turtle.forward(distance)
        self.position += distance
