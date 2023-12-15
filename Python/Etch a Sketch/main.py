from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def rotate_clockwise():
    timmy.right(5)


def rotate_counter_clockwise():
    timmy.left(5)


def clear_screen():
    timmy.penup()
    timmy.clear()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
