from turtle import Turtle

alignment = "center"
font = ("Courier", 15, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 280)
        self.score = 0
        self.write_out()

    def write_out(self):
        self.clear()
        self.write(f"Score: {self.score}", align = alignment, font = font)

    def increase(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over\nScore: {self.score}", align = alignment, font = font)