from turtle import Turtle

STARTING_POSITION = [(0, 0)]


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.created_body()

    def created_body(self):
        for position in STARTING_POSITION:
            self.add_body(position)

    def add_body(self, position):
        new_segment = Turtle(shape="classic")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # def extend(self):
