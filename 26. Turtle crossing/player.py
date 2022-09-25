from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):   # as much as the screen will update, the number of the cars will be added on the screen
        self.shape("turtle")
        self.fillcolor("peru")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        y_new = self.ycor() + MOVE_DISTANCE
        self.goto(x=0, y=y_new)

    def is_at_final(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_back_position(self):
        self.goto(STARTING_POSITION)
