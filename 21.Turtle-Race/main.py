from turtle import Turtle, Screen
import random

is_race_on = False  # right now the race is not started

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_guess = ''
while user_guess not in colors:
    user_guess = screen.textinput(title="Make a bet", prompt="Which color would win the race? Enter a color: ")
y_position = [-100, -50, 0, 50, 100, 150]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

# this code will trigger when the user bet's on the turtle
if user_guess:
    is_race_on = True  # after assigning is_race_on = True, finally the race will start.

while is_race_on:
    for turtle in all_turtle:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_guess == winner:
                print(f"You Win the bet, {winner} Turtle has won the race")
            else:
                print(f"You Lost the bet, {winner} Turtle has won the race")

screen.exitonclick()
