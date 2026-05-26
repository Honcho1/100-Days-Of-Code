import random
from turtle import Turtle, Screen


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_shape(turtle, sides, side_length=100):
    turtle.color(random_color())
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(side_length)
        turtle.right(angle)



if __name__ == "__main__":
    screen = Screen()
    screen.colormode(255)

    tim = Turtle()
    tim.pensize(3)
    tim.speed("fastest")

    for sides in range(3, 11):
        tim.penup()
        tim.home()
        tim.setheading(0)
        tim.pendown()
        draw_shape(tim, sides, 100)

    screen.exitonclick()