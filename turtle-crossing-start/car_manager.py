import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        car.goto(300, random.randint(-240, 240))
        self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars[:]:
            car.setx(car.xcor() - STARTING_MOVE_DISTANCE)
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)
