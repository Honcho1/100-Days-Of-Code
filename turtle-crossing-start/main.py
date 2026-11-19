import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()
car_timer = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_timer += 1
    if car_timer % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_level()
    for car in car_manager.all_cars:
        if (abs(player.xcor() - car.xcor()) < 30
                and abs(player.ycor() - car.ycor()) < 20):
            game_is_on = False
            scoreboard.game_over()
            break
    screen.update()
