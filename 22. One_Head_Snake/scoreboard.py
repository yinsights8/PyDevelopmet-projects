from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("courier", 12, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as data:
            self.highscore = int(data.read())
        self.color("black")
        self.penup()
        self.goto(x=0, y=280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | Highscore: {self.highscore}", align=ALIGNMENT,
                   font=("courier", 15, "normal"))

    def keepscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode = 'w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=("courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
