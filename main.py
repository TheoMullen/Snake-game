import time

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

keep_going = True
while keep_going:
    snake.move()
    screen.update()
    time.sleep(0.1)


    # Detect contact with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
        scoreboard.write_out()

    # Detect contact with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        keep_going = False
        scoreboard.game_over()

    # Detect contact with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            keep_going = False
            scoreboard.game_over()



screen.exitonclick()
