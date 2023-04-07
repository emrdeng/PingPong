import turtle
import winsound
import random

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("#567189")
wn.setup(width = 800, height = 600, startx = 0, starty = 0)
wn.tracer(0)

#Dictionary:
settings = {
    "on_menu_screen": True,
    "on_game_screen": False,
    "ball_speed": "Normal",
    "paddle_size": "Normal",
}

wn.update()

# Declare the turtles as global variables
global menu, settings_button, ball_speed_title, ball_speed_normal, ball_speed_fast, paddle_size_title, paddle_size_normal, paddle_size_tiny

# Menu Turtle:
menu = turtle.Turtle()
menu.hideturtle()
menu.penup()
menu.goto(0, 200)
menu.color("white")

# Menu Title Text:
menu.write("Ping Pong", align="center", font=("Courier", 48, "bold"))
menu.goto(0, 150)
menu.write("Press spacebar to start!", align="center", font=("Courier", 20, "normal"))
menu.goto(0, 125)
menu.write("Press backspace to exit the game!", align="center", font=("Courier", 10, "normal"))

# Create the settings button:
settings_button = turtle.Turtle()
settings_button.hideturtle()
settings_button.penup()
settings_button.goto(-280, 50)
settings_button.write("Settings:", align="center", font=("Courier", 26, "bold"))

# Create the ball speed choices:
ball_speed_title = turtle.Turtle()
ball_speed_title.hideturtle()
ball_speed_title.penup()
ball_speed_title.goto(-230, 5)
ball_speed_title.write("Ball Speed:", align="center", font=("Courier", 20, "bold"))

ball_speed_normal = turtle.Turtle()
ball_speed_normal.hideturtle()
ball_speed_normal.penup()
ball_speed_normal.goto(-280,-40)
if settings["ball_speed"] == "Normal":
    ball_speed_normal.color("white")
else:
    ball_speed_normal.color("black")
ball_speed_normal.write("Normal", align="left", font=("Courier", 18, "bold"))

ball_speed_fast = turtle.Turtle()
ball_speed_fast.hideturtle()
ball_speed_fast.penup()
ball_speed_fast.goto(-280, -90)
ball_speed_fast.write("Fast", align="left", font=("Courier", 18, "bold"))

# Create the ball speed choices:
paddle_size_title = turtle.Turtle()
paddle_size_title.hideturtle()
paddle_size_title.penup()
paddle_size_title.goto(20, 5)
paddle_size_title.write("Paddle Size:", align="center", font=("Courier", 20, "bold"))

paddle_size_normal = turtle.Turtle()
paddle_size_normal.hideturtle()
paddle_size_normal.penup()
paddle_size_normal.goto(-30, -40)
if settings["paddle_size"] == "Normal":
    paddle_size_normal.color("white")
else:
    paddle_size_normal.color("black")
paddle_size_normal.write("Normal", align="left", font=("Courier", 18, "bold"))

paddle_size_tiny = turtle.Turtle()
paddle_size_tiny.hideturtle()
paddle_size_tiny.penup()
paddle_size_tiny.goto(-30, -90)
paddle_size_tiny.write("That 70's Show Difficult", align="left", font=("Courier", 18, "bold"))

def manage_settings(x, y):
    # This is the if function that covers CLICKING ON THE FAST BALL SPEED OPTION:
    if (x >= -280 and x <= -224) and (y >= -87 and y <= -64):
        settings["ball_speed"] = "Fast"
        ball_speed_normal.clear()
        ball_speed_normal.penup()
        ball_speed_normal.goto(-280, -40)

        ball_speed_fast.clear()
        ball_speed_fast.penup()
        ball_speed_fast.goto(-280, -90)

        if settings["ball_speed"] == "Normal":
            ball_speed_normal.color("white")
            ball_speed_fast.color("black")
        else:
            ball_speed_normal.color("black")
            ball_speed_fast.color("white")
        ball_speed_fast.write("Fast", align="left", font=("Courier", 18, "bold"))
        ball_speed_normal.write("Normal", align="left", font=("Courier", 18, "bold"))
    # This is the if function that covers CLICKING ON THE NORMAL BALL SPEED OPTION:
    if (-282 <= x <= -199) and (-36 <= y <= -16):
        settings["ball_speed"] = "Normal"
        ball_speed_normal.clear()
        ball_speed_normal.penup()
        ball_speed_normal.goto(-280, -40)

        ball_speed_fast.clear()
        ball_speed_fast.penup()
        ball_speed_fast.goto(-280, -90)

        if settings["ball_speed"] == "Normal":
            ball_speed_normal.color("white")
            ball_speed_fast.color("black")
        else:
            ball_speed_normal.color("black")
            ball_speed_fast.color("white")

        ball_speed_fast.write("Fast", align="left", font=("Courier", 18, "bold"))
        ball_speed_normal.write("Normal", align="left", font=("Courier", 18, "bold"))
    # This is the if function that covers CLICKING ON THE NORMAL PADDLE SIZE OPTION:
    if (-31 <= x <= 49) and (-36 <= y <= -16):
        settings["paddle_size"] = "Normal"
        paddle_size_normal.clear()
        paddle_size_normal.penup()
        paddle_size_normal.goto(-30, -40)

        paddle_size_tiny.clear()
        paddle_size_tiny.penup()
        paddle_size_tiny.goto(-30, -90)

        if settings["paddle_size"] == "Normal":
            paddle_size_normal.color("white")
            paddle_size_tiny.color("black")
        else:
            paddle_size_normal.color("black")
            paddle_size_tiny.color("white")

        paddle_size_tiny.write("That 70's Show Difficult", align="left", font=("Courier", 18, "bold"))
        paddle_size_normal.write("Normal", align="left", font=("Courier", 18, "bold"))
    # This is the if function that covers CLICKING ON THE SMALL PADDLE SIZE OPTION:
    if (-31 <= x <= 304) and (-85 <= y <= -67):
        settings["paddle_size"] = "Tiny"
        paddle_size_normal.clear()
        paddle_size_normal.penup()
        paddle_size_normal.goto(-30, -40)

        paddle_size_tiny.clear()
        paddle_size_tiny.penup()
        paddle_size_tiny.goto(-30, -90)

        if settings["paddle_size"] == "Tiny":
            paddle_size_normal.color("black")
            paddle_size_tiny.color("white")
        else:
            paddle_size_normal.color("white")
            paddle_size_tiny.color("black")

        paddle_size_tiny.write("That 70's Show Difficult", align="left", font=("Courier", 18, "bold"))
        paddle_size_normal.write("Normal", align="left", font=("Courier", 18, "bold"))

def play_game(wn):
    # Score:
    scoreA = 0
    scoreB = 0

    # Paddle A
    paddleA = turtle.Turtle()
    paddleA.speed(0)
    paddleA.shape("square")
    paddleA.color("white")
    paddleA.penup()
    paddleA.goto(-350, 0)
    if settings["paddle_size"] == "Normal":
        paddleA.shapesize(5, 1)
        half_length = 50
    else:
        paddleA.shapesize(2, 1)
        half_length = 20

    # Paddle B
    paddleB = turtle.Turtle()
    paddleB.speed(0)
    paddleB.shape("square")
    paddleB.color("white")
    paddleB.penup()
    paddleB.goto(350, 0)
    if settings["paddle_size"] == "Normal":
        paddleB.shapesize(5, 1)
        half_length = 50
    else:
        paddleB.shapesize(2, 1)
        half_length = 20

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    neg_or_pos = [-1, 1]
    if settings["ball_speed"] == "Normal":
        ball.dx = random.uniform(.05, .15) * random.choice(neg_or_pos)
        ball.dy = random.uniform(.05, .15) * random.choice(neg_or_pos)
    else:
        ball.dx = random.uniform(.2, .25) * random.choice(neg_or_pos)
        ball.dy = random.uniform(.2, .25) * random.choice(neg_or_pos)

    # Pen:
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    score_title = f"Player A: {scoreA}  Player B: {scoreB}"
    pen.write(score_title, align="center", font=("Courier", 24, "normal"))

    # Function
    # Paddle A Movement
    def paddleA_up():
        y = paddleA.ycor()
        if settings["paddle_size"] == "Normal":
            if y + 20 < 250:
                y += 20
        else:
            if y + 20 < 300:
                y += 20
        paddleA.sety(y)

    def paddleA_down():
        y = paddleA.ycor()
        if settings["paddle_size"] == "Normal":
            if y - 20 > -250:
                y -= 20
        else:
            if y - 20 > -300:
                y -= 20
        paddleA.sety(y)

    # PaddleB Movement:
    def paddleB_up():
        y = paddleB.ycor()
        if settings["paddle_size"] == "Normal":
            if y + 20 < 250:
                y += 20
        else:
            if y + 20 < 300:
                y += 20
        paddleB.sety(y)

    def paddleB_down():
        y = paddleB.ycor()
        if settings["paddle_size"] == "Normal":
            if y - 20 > -250:
                y -= 20
        else:
            if y - 20 > -300:
                y -= 20
        paddleB.sety(y)

    wn.listen()
    wn.onkeypress(paddleA_up, "w")
    wn.onkeypress(paddleA_down, "s")
    wn.onkeypress(paddleB_up, "Up")
    wn.onkeypress(paddleB_down, "Down")

    # Main Game Loop
    while settings["on_game_screen"]:
        wn.update()

        # Move the ball:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border Checking:
        # Top Border
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        # Bottom Border:
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        # Right Border:
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            scoreA += 1
            pen.clear()
            score_title = f"Player A: {scoreA}  Player B: {scoreB}"
            pen.write(score_title, align="center", font=("Courier", 24, "normal"))
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        # Left Border:
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            scoreB += 1
            pen.clear()
            score_title = f"Player A: {scoreA}  Player B: {scoreB}"
            pen.write(score_title, align="center", font=("Courier", 24, "normal"))
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # Paddle hitting the ball
        # Paddle A
        paddleA_yMin = paddleA.ycor() - half_length
        paddleA_yMax = paddleA.ycor() + half_length

        if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() <= paddleA_yMax and ball.ycor() >= paddleA_yMin:
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # Paddle B
        paddleB_yMin = paddleB.ycor() - half_length
        paddleB_yMax = paddleB.ycor() + half_length

        if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() <= paddleB_yMax and ball.ycor() >= paddleB_yMin:
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

# Define a function to handle the spacebar key press
def change_screens():
    if settings["on_menu_screen"]:
        settings["on_menu_screen"] = False
        settings["on_game_screen"] = True
        menu.clear()
        settings_button.clear()
        ball_speed_title.clear()
        ball_speed_normal.clear()
        ball_speed_fast.clear()
        paddle_size_normal.clear()
        paddle_size_tiny.clear()
        paddle_size_title.clear()
        play_game(wn)

def leave():
    wn.bye()

# Bind the spacebar key to the start_game function
wn.onkeypress(change_screens, "space")
wn.onscreenclick(manage_settings, 1)
wn.onkeypress(leave, "BackSpace")

# Start the event loop
wn.listen()
wn.mainloop()

