import turtle
import time

# ---------------------------
# Screen Setup
# ---------------------------
win = turtle.Screen()
win.title("Ping Pong Game by YOU")
win.bgcolor("black")
win.setup(width=800, height=600)

# ---------------------------
# Score Variables
# ---------------------------
score_a = 0
score_b = 0

# ---------------------------
# Paddle A
# ---------------------------
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# ---------------------------
# Paddle B
# ---------------------------
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ---------------------------
# Ball
# ---------------------------
ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 7.00 * 1.05
ball.dy = 7.00 * 1.05

# ---------------------------
# Score Display
# ---------------------------
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# ---------------------------
# Winner Display
# ---------------------------
winner_display = turtle.Turtle()
winner_display.speed(0)
winner_display.color("yellow")
winner_display.penup()
winner_display.hideturtle()
winner_display.goto(0, 0)

# ---------------------------
# Paddle Movement Functions
# ---------------------------
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        paddle_b.sety(y - 20)

# ---------------------------
# Keyboard Bindings
# ---------------------------
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# ---------------------------
# Function to Update Score Display
# ---------------------------
def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}",
                        align="center", font=("Courier", 24, "normal"))

# ---------------------------
# Game Loop
# ---------------------------
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom wall bounce
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Right wall: Player A scores
    if ball.xcor() > 390:
        score_a += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1.1
        ball.dy *= 1.1

    # Left wall: Player B scores
    if ball.xcor() < -390:
        score_b += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1.1
        ball.dy *= 1.1


    # Paddle collision (Player B)
    if (340 < ball.xcor() < 350 and
        paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.dx *= -1

    # Paddle collision (Player A)
    if (-350 < ball.xcor() < -340 and
        paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.dx *= -1

    # Check for Winner
    if score_a == 10 or score_b == 10:
        winner = "Player A" if score_a == 10 else "Player B"
        winner_display.write(f"Winner: {winner}", align="center", font=("Courier", 36, "bold"))
        time.sleep(3)
        break
