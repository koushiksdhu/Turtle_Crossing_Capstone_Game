from turtle import Turtle
import random
import time

# CONSTANTS:
COLORS = ["red", "green", "blue", "yellow", "purple", "aqua", "orange"]
SPEED = 5

class Cars():
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = SPEED        
        
    def create_cars(self):
        value = random.randint(1, 6)
        if value == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def speed_up(self):
        self.car_speed += SPEED
          

