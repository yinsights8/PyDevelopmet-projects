from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.title("Pong - The Arcade Game")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 287 or ball.ycor() < -287:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if R paddle misses the ball
    if ball.xcor() > 380:
        scoreboard.score_l_increase()
        ball.reset_position()

    # if L paddle misses the ball
    if ball.xcor() < -380:
        scoreboard.score_r_increase()
        ball.reset_position()


screen.exitonclick()
