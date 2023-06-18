from turtle import Turtle

# CONSTANTS:
ALIGNMENT = "right"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-190, 270)
        self.level = 1
        self.write(f"Level: {self.level}", align = ALIGNMENT, font = FONT)
        
    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align = ALIGNMENT, font = FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center", font = FONT)
        