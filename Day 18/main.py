import random
from turtle import Turtle, Screen


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_random_walk(turtle, steps, step_length=20):
    directions = [0, 90, 180, 270]
    turtle.pensize(5)
    turtle.speed("fastest")
    turtle.hideturtle()
    for _ in range(steps):
        turtle.color(random_color())
        turtle.setheading(random.choice(directions))
        turtle.forward(step_length)


if __name__ == "__main__":
    screen = Screen()
    screen.colormode(255)

    tim = Turtle()
    draw_random_walk(tim, 200, 20)

    screen.exitonclick()