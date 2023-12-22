import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
screen.tracer(0)
segments = []
for position in starting_positions:
    new_snake_segment = Turtle(shape="square")
    new_snake_segment.color("white")
    new_snake_segment.penup()
    new_snake_segment.goto(position)
    segments.append(new_snake_segment)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(segments)-1, 0, -1):
        x = segments[segment - 1].xcor()
        y = segments[segment - 1].ycor()
        segments[segment].goto(x, y)

screen.exitonclick()
