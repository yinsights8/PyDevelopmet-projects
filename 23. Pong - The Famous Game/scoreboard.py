from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.score_l}", align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.score_r}", align="center", font=("courier", 80, "normal"))

    def score_l_increase(self):
        self.score_l += 1
        self.score_update()

    def score_r_increase(self):
        self.score_r += 1
        self.score_update()