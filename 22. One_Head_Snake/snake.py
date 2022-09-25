from turtle import Turtle

STARTING_POSITION = [(0, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.created_body()
        self.head = self.segments[0]

    def created_body(self):
        for position in STARTING_POSITION:
            self.s_head(position)
            self.add_segments(position)

    def s_head(self, position):
        head = Turtle(shape="classic")
        head.shapesize(stretch_len=2, stretch_wid=3)
        head.color("black")
        head.penup()
        head.goto(position)
        self.segments.append(head)

    def add_segments(self, position):
        snake = Turtle(shape="circle")
        snake.shapesize(stretch_len=1, stretch_wid=0.9)
        snake.color("alice blue")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend_body(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for snake in range(len(self.segments) - 1, 0, -1):
            x_snake = self.segments[snake - 1].xcor()
            y_snake = self.segments[snake - 1].ycor()
            self.segments[snake].goto(x_snake, y_snake)
        self.segments[0].forward(20)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.created_body()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def rt(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def lt(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reappear(self):
        if self.head.xcor() > 290:
            self.head.setx(-290)

        if self.head.xcor() < -290:
            self.head.setx(290)

        if self.head.ycor() > 290:
            self.head.sety(-290)

        if self.head.ycor() < -290:
            self.head.sety(290)
