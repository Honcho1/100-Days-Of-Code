from turtle import Turtle, Screen


def draw_dashed_line(length, dash_length=10, gap_length=10):
    tim = Turtle()
    tim.color("red")
    tim.pensize(2)
    for _ in range(length // (dash_length + gap_length)):
        tim.forward(dash_length)
        tim.penup()
        tim.forward(gap_length)
        tim.pendown()


if __name__ == "__main__":
    screen = Screen()
    draw_dashed_line(200)
    screen.exitonclick()