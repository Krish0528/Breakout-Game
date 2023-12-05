from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 250)
        self.write(f"Score: {self.score}", align="center", font=("comic sans", 24, "normal"))

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()
