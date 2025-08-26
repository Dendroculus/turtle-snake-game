from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, fruits):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.fruits = fruits
        self.refresh()
    
    def refresh(self):
        # Pick random fruit image
        fruit = random.choice(self.fruits)
        self.shape(fruit)

        # Prevent spawning behind scoreboard (reserved top area ~40px)
        x = random.randint(-260, 260)
        y = random.randint(-260, 230)
        self.goto(x, y)
