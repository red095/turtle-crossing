from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.update_scroreboard()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT)
    def update_scroreboard(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scroreboard()



