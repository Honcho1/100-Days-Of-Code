from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def move_paddle_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)

def move_paddle_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)

screen.listen()
screen.onkeypress(move_paddle_up, "Up")
screen.onkeypress(move_paddle_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()










screen.exitonclick()