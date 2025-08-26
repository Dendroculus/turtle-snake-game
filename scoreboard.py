from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")  # text color
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def draw_rectangle(self, x, y, width, height, color):
        self.goto(x, y)
        self.fillcolor(color)
        self.pendown()
        self.begin_fill()
        for _ in range(2):
            self.forward(width)
            self.right(90)
            self.forward(height)
            self.right(90)
        self.end_fill()
        self.penup()

    def update_scoreboard(self):
        self.clear()
        # Draw soft background rectangle behind score
        box_width = 120
        box_height = 30
        box_x = -box_width // 2
        box_y = 260  # top-left corner of box

        self.draw_rectangle(box_x, box_y, box_width, box_height, "#444444")

        # Move to center of the rectangle (pushed down by 5)
        text_y = box_y - box_height // 2 - 8
        self.goto(0, text_y)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard() 

    def game_over(self):
        self.hideturtle()
        self.penup()

        screen = self.getscreen()
        screen.addshape("gameover.gif")

        go_image = Turtle()
        go_image.hideturtle()
        go_image.penup()
        go_image.goto(0, 0)
        go_image.shape("gameover.gif")
        go_image.showturtle()

        screen.update()  # force the GIF to display immediately

        time.sleep(7)  # match your mp3 duration
