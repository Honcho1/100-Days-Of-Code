from turtle import Turtle, Screen

MOVE_DISTANCE = 20
TURN_ANGLE = 10

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(MOVE_DISTANCE)

def move_backwards():
    tim.backward(MOVE_DISTANCE)

def turn_left():
    # Counterclockwise
    tim.left(TURN_ANGLE)

def turn_right():
    # Clockwise
    tim.right(TURN_ANGLE)

def clear_drawing():
    # Erases all drawings, then returns the turtle to the # centre and resets its heading to the default 
    # (facing right)
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
