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
        with open("data.txt", mode="r") as score_file:
            self.high_score = int(score_file.read())
        self.write_out()


    def write_out(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align = alignment, font = font)

    def increase(self):
        self.score += 1
        self.write_out()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as score_file:
                score_file.write(str(self.score))
            with open("data.txt", mode="r") as score_file:
                self.high_score = int(score_file.read())
        self.score = 0
        self.write_out()

