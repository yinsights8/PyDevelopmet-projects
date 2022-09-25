from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)

    def bounce_y(self):
        # when the ball collides with the wall then the wall of y_move will be -10
        self.y_move *= -1
        # print(self.y_move)       # y_move is going to subtract -10
        # print(self.x_move)       # x_move is going to be constant

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
