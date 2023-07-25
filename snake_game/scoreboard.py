from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        with open("data.txt", mode="r") as data:
            self.highscore = int(data.read())
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} Highscore: {self.highscore}", align="center", font=('Courier', 20, 'normal'))

    def reset_score(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
