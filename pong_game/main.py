from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect when the paddle misses
    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_position()
    elif ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_position()
    screen.update()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0:
        ball.bounce_x()
        ball.increase_speed()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_x()
        ball.increase_speed()

screen.exitonclick()