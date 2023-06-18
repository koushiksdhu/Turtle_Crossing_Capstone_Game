from turtle import Turtle

# CONSTANTS:
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280   # y-coordinates / y-axis.

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("#ffffff")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        
    def reset_position (self):
        self.goto(STARTING_POSITION)
    
    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        return False
        
        
        