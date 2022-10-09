from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-240, 230)
        self.write(f"Player 1 : {self.l_score}", font=("Times New Roman", 20, 'normal'))
        self.goto(100, 230)
        self.write(f"Player 2 : {self.r_score}", font=("Times New Roman", 20, 'normal'))

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def check_point(self):
        if self.l_score == 10:
            return 1
        elif self.r_score == 10:
            return 0

    def l_message(self):
        self.goto(0, 0)
        self.write("GAME OVER\nPlayer 1 WINS!", align="center", font=("Times New Roman", 30, 'normal'))

    def r_message(self):
        self.goto(0, 0)
        self.write("GAME OVER\nPlayer 2 WINS!", align="center", font=("Times New Roman", 30, 'normal'))
