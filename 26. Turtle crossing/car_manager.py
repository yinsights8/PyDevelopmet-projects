from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        dice = random.randint(1, 6)
        if dice == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.fillcolor(random.choice(COLORS))
            y_random = random.randint(-250, 250)   # # #
            new_car.goto(280, y_random)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
