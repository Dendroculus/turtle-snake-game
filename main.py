from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from playsound import playsound
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("Background.png")
screen.title("Snake Game")
screen.tracer(0)

# Register fruit images
fruits = ["apple.gif", "banana.gif", "watermelon.gif"]
for fruit in fruits:
    screen.addshape(fruit)

snake = Snake()
food = Food(fruits)  # pass fruit list
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

def food_eaten():
    if snake.head.distance(food) < 13:
        playsound("eat.mp3", block=False)
        food.refresh()
        score.increase_score()
        return True
    return False
        
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
   
    # Detect Collision with food
    if food_eaten():
        snake.extend()
    
    # Detect collision with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 
        or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        playsound("Gameover.mp3", block=False)
        score.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 10:
            playsound("Gameover.mp3", block=False)
            score.game_over()
            game_is_on = False
     
screen.exitonclick()
