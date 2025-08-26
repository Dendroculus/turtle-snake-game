from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
screen = Screen()
screen.colormode(255)

class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.can_turn = True

        # Add eyes (separate turtles, not part of snake_list)
        self.left_eye = Turtle("circle")
        self.left_eye.shapesize(0.2, 0.2)
        self.left_eye.color("black")
        self.left_eye.penup()

        self.right_eye = Turtle("circle")
        self.right_eye.shapesize(0.2, 0.2)
        self.right_eye.color("black")
        self.right_eye.penup()

        self.update_eyes()

    def create_snake(self):
        colors = [
            (0, 255, 0),   # Head - bright lime
            (0, 200, 0),   # Middle - medium green
            (0, 120, 0)    # Tail - dark green
        ]

        for i in range(3):
            snake = Turtle("square")
            snake.penup()
            snake.goto(x=-20 * i, y=0)
            snake.color(colors[i])
            self.snake_list.append(snake)

        self.can_turn = True

    def move(self):
        for idx in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[idx - 1].xcor()
            new_y = self.snake_list[idx - 1].ycor()
            self.snake_list[idx].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

        # Move eyes with head
        self.update_eyes()
        self.can_turn = True

    def update_eyes(self):
        if self.head.heading() == UP:
            self.left_eye.goto(self.head.xcor() - 5, self.head.ycor() + 10)
            self.right_eye.goto(self.head.xcor() + 5, self.head.ycor() + 10)
        elif self.head.heading() == DOWN:
            self.left_eye.goto(self.head.xcor() - 5, self.head.ycor() - 10)
            self.right_eye.goto(self.head.xcor() + 5, self.head.ycor() - 10)
        elif self.head.heading() == LEFT:
            self.left_eye.goto(self.head.xcor() - 10, self.head.ycor() + 5)
            self.right_eye.goto(self.head.xcor() - 10, self.head.ycor() - 5)
        elif self.head.heading() == RIGHT:
            self.left_eye.goto(self.head.xcor() + 10, self.head.ycor() + 5)
            self.right_eye.goto(self.head.xcor() + 10, self.head.ycor() - 5)

    def extend(self):
        # Color cycle
        colors = [
            (0, 255, 0),   # bright lime
            (0, 200, 0),   # medium green
            (0, 120, 0)    # dark green
        ]

        # Pick color based on length of snake
        color = colors[len(self.snake_list) % len(colors)]

        # Create new body segment
        snake = Turtle("square")
        snake.penup()
        snake.color(color)
        snake.goto(self.snake_list[-1].position())
        self.snake_list.append(snake)


    def up(self):
        if self.head.heading() != DOWN and self.can_turn:
            self.head.setheading(UP)
            self.can_turn = False

    def down(self):
        if self.head.heading() != UP and self.can_turn:
            self.head.setheading(DOWN)
            self.can_turn = False

    def left(self):
        if self.head.heading() != RIGHT and self.can_turn:
            self.head.setheading(LEFT)
            self.can_turn = False

    def right(self):
        if self.head.heading() != LEFT and self.can_turn:
            self.head.setheading(RIGHT)
            self.can_turn = False
