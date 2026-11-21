from pathlib import Path
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
DATA_FILE = Path(__file__).with_name("data.txt")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(DATA_FILE.read_text())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            DATA_FILE.write_text(str(self.high_score))
        self.clear()
        self.update_scoreboard()
