from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def up():
    #tim.setheading(0)
    tim.forward(10)

def down():
    tim.setheading(0)
    tim.back(10)

def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    #tim.left(25)


def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    #tim.right(25)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    #tim.reset()
    # tim.clear()
    # tim.goto(0,0)
    # tim.setheading(0)


screen.listen()
screen.onkey(key="w", fun=up)
screen.onkey(key="s", fun=down)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

print(tim.heading())

screen.exitonclick()
