from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1
        self.levels()

    def levels(self):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.levels()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)




