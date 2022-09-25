import turtle
from turtle import Turtle, Screen
from sanke_body import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("light Green")
turtle.tracer(0)

snake = Snake()
food = Food()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.forward(20)

screen.exitonclick()
