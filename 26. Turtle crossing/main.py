import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("slate gray")
screen.tracer(0)

player = Player()
car_man = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.go_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_man.create_car()  # # #
    car_man.move()

    # Detect when collides with the car
    for car in car_man.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # if player.ycor() > 280:
    #     player.reached_top()
    #     car_man.level_up()

    if player.is_at_final():
        player.go_back_position()
        scoreboard.update_level()
        car_man.level_up()

screen.exitonclick()
