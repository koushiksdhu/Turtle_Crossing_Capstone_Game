from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Turtle Crossing Game - Made by Koushik Sadhu")
screen.bgcolor("#000000")
screen.tracer(0)

player = Player()
car = Cars()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_up, "w")
screen.onkey(player.go_up, "W")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.create_cars()
    car.move()
    screen.update()
    
    # Detect collision of turtle with car:
    for one_car in car.all_cars:
        if one_car.distance(player) < 30:
            score.game_over()
            game_is_on = False
    
    # Detect when the player reaches the destination successfully:
    if player.is_at_finish_line():
        player.reset_position()
        score.clear()
        score.update_level()
        car.speed_up()

    





screen.exitonclick()


