import random
from turtle import Turtle, Screen


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



def draw_spirograph(turtle, radius=100, gap_size=5):
    turtle.pensize(2)
    turtle.speed("fastest")
    count = int(360 / gap_size)
    for _ in range(count):
        turtle.color(random_color())
        turtle.circle(radius)
        turtle.setheading(turtle.heading() + gap_size)


if __name__ == "__main__":
    screen = Screen()
    screen.colormode(255)

    tim = Turtle()

    draw_spirograph(tim, radius=100, gap_size=5)

    screen.exitonclick()
