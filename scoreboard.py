from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.l_score}", align="center", font=FONT)

        self.goto(100, 250)
        self.write(f"{self.r_score}", align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_board()

    def r_point(self):
        self.r_score += 1
        self.update_board()
