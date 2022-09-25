from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# 0. set up a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
# x_position = [0, 40, 20]
screen.tracer(0)  # we turn off the tracer, it will pop up a black screen, until we update the screen in further in our
scoreboard = Scoreboard()

snake = Snake()
# create Food
food = Food()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with a food
    if snake.head.distance(food) < 15:  # food < head = 15
        food.refresh()
        snake.extend_size()
        scoreboard.add_score()

    # Detect Wall Collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        #game_is_on = False
        scoreboard.reset()
        snake.reset()
        #scoreboard.game_over()

    # Detect Tail Collision
    # if the snack.head.distance(segmets) < 10:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            scoreboard.reset()
            snake.reset()
            #scoreboard.game_over()
            # scoreboard.game_over()

screen.exitonclick()
