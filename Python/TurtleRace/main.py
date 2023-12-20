import random
from turtle import Turtle, Screen

from race_turtle import RaceTurtle

screen = Screen()
colors_in_rainbow = ["red", "orange", "yellow", "green", "blue", "purple", "violet"]
race_turtles = []
y = 0
got_to_finish_line = False
screen.setup(width=300, height=400)
for n in range(0, 7 - 1):
    race_turtle = RaceTurtle(Turtle(), colors_in_rainbow[n])
    race_turtle.turtle.setpos(-200, y)
    race_turtles.append(race_turtle)
    y += 20
your_bet = screen.textinput(title="Race Turtle Selection", prompt="Choose your Race turtle's color").lower()
while not got_to_finish_line:
    for RaceTurtle in race_turtles:
        RaceTurtle.forward_to_line(random.randint(0, 10))

        if RaceTurtle.position >= 500:
            winner = RaceTurtle.color
            got_to_finish_line = True
if winner == your_bet:
    print(f"Your turtle won, the winner is {winner}")
else:
    print(f"Your turtle lost, the winner is {winner}")
screen.exitonclick()
