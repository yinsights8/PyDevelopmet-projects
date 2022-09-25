import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        x_random = random.randint(-280, 280)
        y_random = random.randint(-280, 280)
        self.goto(x_random, y_random)
