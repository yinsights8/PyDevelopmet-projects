from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("dim gray")
screen.setup(height=600, width=600)
screen.title("The Snake Game")
screen.tracer(0)

# user_input = ""
# while user_input not in ["hard", "easy"]:
#     user_input = screen.textinput(title="Difficulty Level", prompt="Choose Difficulty Level HARD or EASY: ").lower()


snake = Snake()
snake.hideturtle()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.lt, key="Left")
screen.onkey(fun=snake.rt, key="Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_body()
        scoreboard.increase_score()

    # if user_input == 'easy':
    #     snake.reappear()

    # else:

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_snake()
            scoreboard.keepscore()
            # scoreboard.game_over()
            # game_on = False
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        snake.reset_snake()
        scoreboard.keepscore()
        # scoreboard.game_over()
        # game_on = False

screen.exitonclick()
