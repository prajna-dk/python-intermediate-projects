from turtle import Turtle

class Score(Turtle):
    def __init__(self, shape = "classic"):
        super().__init__(shape)
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            arg= f"Score is {self.score}",
            move= False,
            align = "center",
            font=("Arial", 18, "normal")
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def on_game_over(self):
        self.goto(0,0)
        self.write(
            arg= "GAME OVER",
            move= False,
            align = "center",
            font=("Arial", 20, "normal")
        )