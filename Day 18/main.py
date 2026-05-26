from turtle import Turtle, Screen


def draw_square(size):
    tim = Turtle()
    tim.color("blue")
    tim.pensize(3)
    for _ in range(4):
        tim.forward(size)
        tim.right(90)


if __name__ == "__main__":
    screen = Screen()
    draw_square(100)
    screen.exitonclick()