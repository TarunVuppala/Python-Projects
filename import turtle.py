import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=1.0, height=1.0)
wn.tracer(0)  # Turns off the screen updates

# Wall dimensions
wall_x = int(wn.window_width() / 2) - 40
wall_y = int(wn.window_height() / 2) - 40


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-wall_x + 20, wall_x - 20), random.randint(-wall_y + 20, wall_y - 20))

segments = []

# Nav bar
nav = turtle.Turtle()
nav.speed(0)
nav.color("white")
nav.penup()
nav.hideturtle()
nav.goto(0, wall_y - 20)
nav.write("Score: 0", align="center", font=("Courier", 24, "normal"))
nav.goto(0, wall_y - 50)
nav.write("High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        head.setheading(90)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        head.setheading(270)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        head.setheading(180)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        head.setheading(0)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

def quit_game():
    wn.bye()

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if (
        head.xcor() > wall_x
        or head.xcor() < -wall_x
        or head.ycor() > wall_y
        or head.ycor() < -wall_y
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        delay = 0.1

        nav.clear()
        nav.goto(0, wall_y - 20)
        nav.write(
            "Score: {}  High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Check for a collision with the food
    if head.distance(food) < 20:
        x = random.randint(-wall_x + 20, wall_x - 20)
        y = random.randint(-wall_y + 20, wall_y - 20)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        score += 10

        if score > high_score:
            high_score = score

        nav.clear()
        nav.goto(0, wall_y - 20)
        nav.write(
            "Score: {}  High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1

            nav.clear()
            nav.goto(0, wall_y - 20)
            nav.write(
                "Score: {}  High Score: {}".format(score, high_score),
                align="center",
                font=("Courier", 24, "normal"),
            )

    time.sleep(delay)

wn.mainloop()

