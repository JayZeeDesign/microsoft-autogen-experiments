# filename: pong.py
import turtle
import time

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Score var
score_a = 0
score_b = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Moving the paddles
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
        paddle_b.sety(y)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")
win.onkeypress(turtle.bye, "q")  # New keyboard binding for quit

# Main game loop
while True:
    try:
        win.update()

        # Ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collision
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Paddle collision
        if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
            ball.color("blue")
            ball.dx *= -1

        elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
            ball.color("red")
            ball.dx *= -1

        # Missed ball paddle B
        if ball.xcor() > 390:
            score_a += 1
            ball.goto(0, 0)
            ball.dy *= -1
            ball.color("white")
            score_display.clear()
            score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            time.sleep(1)

        # Missed ball paddle A
        if ball.xcor() < -390:
            score_b += 1
            ball.goto(0, 0)
            ball.dy *= -1
            ball.color("white")
            score_display.clear()
            score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            time.sleep(1)

        # Game over
        if score_a == 10:
            score_display.goto(0, 0)
            score_display.write("Player A Wins!", align="center", font=("Courier", 72, "normal"))
            ball.goto(1000,1000)  # Removes the ball from the screen
            break

        if score_b == 10:
            score_display.goto(0, 0)
            score_display.write("Player B Wins!", align="center", font=("Courier", 72, "normal"))
            ball.goto(1000,1000) # Removes the ball from the screen
            break

    except turtle.Terminator:  # Exception handler in case of exit using 'q'
        print("\nGame closed by the player")
        break