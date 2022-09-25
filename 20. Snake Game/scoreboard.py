from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.content = 0
        self.score = 0
        with open("data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} | High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
