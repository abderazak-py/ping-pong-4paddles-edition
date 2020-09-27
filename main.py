import turtle

wind = turtle.Screen()
wind.title("Ping Pong by abdocraft")
wind.bgcolor("yellow")
wind.setup(width=800, height=600)
wind.tracer(0)

# stick1 player 1
stick1 = turtle.Turtle()
stick1.speed(0)
stick1.shape("square")
stick1.color("blue")
stick1.shapesize(stretch_wid=5, stretch_len=1)
stick1.penup()
stick1.goto(-350, 0)

# stick2 player 2
stick2 = turtle.Turtle()
stick2.speed(0)
stick2.shape("square")
stick2.color("red")
stick2.shapesize(stretch_wid=5, stretch_len=1)
stick2.penup()
stick2.goto(350, 0)

# stick3 player 1
stick3 = turtle.Turtle()
stick3.speed(0)
stick3.shape("square")
stick3.color("blue")
stick3.shapesize(stretch_wid=1, stretch_len=5)
stick3.penup()
stick3.goto(0, -250)

# stick4 player 2
stick4 = turtle.Turtle()
stick4.speed(0)
stick4.shape("square")
stick4.color("red")
stick4.shapesize(stretch_wid=1, stretch_len=5)
stick4.penup()
stick4.goto(0, 250)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")  # change it to square if u have animation error with ball
ball.color("green")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 - Player 2: 0", align="center", font=("Courier", 24, "normal"))


# functions
def stick1_up():
    y = stick1.ycor()
    y += 20
    stick1.sety(y)


def stick1_down():
    y = stick1.ycor()
    y -= 20
    stick1.sety(y)


def stick2_up():
    y = stick2.ycor()
    y += 20
    stick2.sety(y)


def stick2_down():
    y = stick2.ycor()
    y -= 20
    stick2.sety(y)


def stick3_up():
    x = stick3.xcor()
    x += 20
    stick3.setx(x)


def stick3_down():
    x = stick3.xcor()
    x -= 20
    stick3.setx(x)


def stick4_up():
    x = stick4.xcor()
    x += 20
    stick4.setx(x)


def stick4_down():
    x = stick4.xcor()
    x -= 20
    stick4.setx(x)


# keyboard
wind.listen()
wind.onkeypress(stick1_up, "z")
wind.onkeypress(stick1_down, "s")
wind.onkeypress(stick2_up, "Up")
wind.onkeypress(stick2_down, "Down")
wind.onkeypress(stick3_up, "d")
wind.onkeypress(stick3_down, "q")
wind.onkeypress(stick4_up, "Right")
wind.onkeypress(stick4_down, "Left")

while True:
    wind.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball x walls ><
    if ball.ycor() > 286:  # player 1
        score1 += 1
        score.clear()
        score.write("Player 1: {} - Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dy *= -1
    if ball.ycor() < -283:  # player 2
        score2 += 1
        score.clear()
        score.write("Player 1: {} - Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dy *= -1
    if ball.xcor() > 383:  # player 1
        score1 += 1
        score.clear()
        score.write("Player 1: {} - Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -386:  # player 2
        score2 += 1
        score.clear()
        score.write("Player 1: {} - Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # ball x stick
    if -330 > ball.xcor() > -345 and stick1.ycor() + 40 > ball.ycor() > stick1.ycor() - 40:
        ball.setx(-330)
        ball.dx *= -1
    if 330 < ball.xcor() < 345 and stick2.ycor() + 40 > ball.ycor() > stick2.ycor() - 40:
        ball.setx(330)
        ball.dx *= -1
    if -230 > ball.ycor() > -245 and stick3.xcor() + 40 > ball.xcor() > stick3.xcor() - 40:
        ball.sety(-230)
        ball.dy *= -1
    if 230 < ball.ycor() < 245 and stick4.xcor() + 40 > ball.xcor() > stick4.xcor() - 40:
        ball.sety(230)
        ball.dy *= -1
