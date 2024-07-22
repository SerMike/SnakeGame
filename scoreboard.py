from turtle import Turtle

SCORE = -1
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        global SCORE
        SCORE += 1
        self.clear()
        self.write(f"Score: {SCORE}", align="center", font=("Courier", 18, "normal"))
