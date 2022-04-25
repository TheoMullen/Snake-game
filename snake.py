import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in positions:
            self.add_segment(position)

    def move(self):
        for _ in range(len(self.segments) - 1, 0, -1):
            x = self.segments[_ - 1].xcor()
            y = self.segments[_ - 1].ycor()
            self.segments[_].goto(x, y)
        self.head.forward(move_distance)

    def add_segment(self, position):
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.goto(position)
        self.segments.append(block)
        screen.update()


    def extend(self):
        self.add_segment(self.segments[-1].position())



    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)


