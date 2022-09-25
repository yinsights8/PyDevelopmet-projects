from turtle import Turtle

COLORS = ["red", "yellow", "blue"]
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_size(self):
        # add_segments at the end of the function
        self.add_segments(self.segments[-1].position()) # position() it is a method in turtle module

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # thi is in reverse order [(-40, 0),(-20, 0),(0, 0)]
            new_x = self.segments[seg_num - 1].xcor()  # this is second last segment i.e (-20, 0)
            new_y = self.segments[seg_num - 1].ycor()  # this is third last segment i.e (0,0)
            self.segments[seg_num].goto(new_x, new_y)  # segments[seg_num] its a last segment # i.e = (-40, 0) == len(self.segments) - 1

        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
