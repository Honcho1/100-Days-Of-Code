from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.goto(position)























screen.exitonclick()