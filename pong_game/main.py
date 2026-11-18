from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.speed(0)
paddle.goto(350, 0)
paddle.speed(3)

def move_paddle_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)

def move_paddle_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)

screen.listen()
screen.onkeypress(move_paddle_up, "Up")
screen.onkeypress(move_paddle_down, "Down")










screen.exitonclick()