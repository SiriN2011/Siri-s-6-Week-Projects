import turtle
import time

# ---------------------------
# Screen Setup
# ---------------------------
win = turtle.Screen()
win.title("Ping Pong Game by YOU") #screen title
win.bgcolor("black") #screen background color
win.setup(width=800, height=600) #screen background size

# ---------------------------
# Score Variables
# ---------------------------
score_a = 0
score_b = 0

# ---------------------------
# Paddle A
# ---------------------------
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of paddle A
paddle_a.shape("square") #shape of the backgroud
paddle_a.color("red") #color of the background
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #size of the background
paddle_a.penup()
paddle_a.goto(-350, 0) #coordinates of paddle A on the screen

# ---------------------------
# Paddle B
# ---------------------------
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of paddle B
paddle_b.shape("square") #shape of the background
paddle_b.color("red") #color of the background
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #size of the background
paddle_b.penup()
paddle_b.goto(350, 0) #coordinates of the background

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
# This displayes how the score should be displayed on the screen
# ---------------------------
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# ---------------------------
# This displays how the "winner" should be displayed on the screen
# ---------------------------
winner_display = turtle.Turtle()
winner_display.speed(0)
winner_display.color("yellow")
winner_display.penup()
winner_display.hideturtle()
winner_display.goto(0, 0)

# ---------------------------
# Paddle Movement Functions on the screen
# ---------------------------
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        paddle_a.sety(y - 20)
        #Checks the paddle's current vertical location and moves it up and down 20 pixels when you clcik a button

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)
        #Moves paddle B up 20 pixels

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        paddle_b.sety(y - 20)
        #Moves paddle B down 20 units and makes sure it doesn't move off the screen

# ---------------------------
# Keys to move paddle a and b up, down, left, and right
# ---------------------------
win.listen()
win.onkeypress(paddle_a_up, "w") #Moves Paddle A up when "w" key is pressed
win.onkeypress(paddle_a_down, "s") #Moves Paddle A down when "s" key is pressed
win.onkeypress(paddle_b_up, "Up") #Moves Paddle B up when "Up" key is pressed
win.onkeypress(paddle_b_down, "Down") #Moves Paddle B up when "Down" key is pressed

# ---------------------------
# Function to Update Score Display
# ---------------------------
def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}",
                        align="center", font=("Courier", 24, "normal"))
# Aligns the score in the center of the screen horizontally
# ---------------------------
# Game Loop
# Bouncs the ball off the wal and keeps track of the score
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
