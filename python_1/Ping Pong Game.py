import turtle

# Screen setup
win = turtle.Screen()   # turtle is a library ; it is also a command
win.title("Ping Pong Game by YOU")
win.bgcolor("black")
win.setup(width=800, height=600)

# Score
score_a = 0
score_b = 0

# When Player A scores
score_a += 1.  # adds one point to players score

# When Player B scores
score_b += 1   # adds one point to players score

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # animation speed
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # 100px tall
paddle_a.penup() # stops drawing
paddle_a.goto(-350, 0) # moves the turtle to x= -350, y=0 position on the screen

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # animation 
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() # stops drawing
paddle_b.goto(350, 0)  # moves the paddle directly to the position

# Ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("white")
ball.penup() # stops drawing
ball.goto(0, 0)
ball.dx = 7.00 # controls ball's speed horizontally
ball.dy = 7.00 # controls ball's speed vertically
ball.dx *= 1.05  # Increase speed by 5%
ball.dy *= 1.05


# Score Display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup() #stops drawing
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Paddle Movement
def paddle_a_up():  #def means define
    y = paddle_a.ycor()
    if y < 250:   #doesn't let the ball go off screen
        paddle_a.sety(y + 20) #if paddle isn't too high paddle moves up 20 pixels

def paddle_a_down():
    y = paddle_a.ycor() #stores the current Y position in the variable "y"
    if y > -240: #prevents the ball from going off the screen
        paddle_a.sety(y - 20) # if the paddle isn't too low it moves it down by 20 steps

def paddle_b_up():
    y = paddle_b.ycor() #stores the current Y position in the variable 'y"
    if y < 250: #checks if the paddle is below the top edge of the screen
        paddle_b.sety(y + 20) #if paddle isn't too high, it moves it up 20 pixels

def paddle_b_down():
    y = paddle_b.ycor() #stores current y position
    if y > -240: #checks if the paddle is above the bottom of the screen 
        paddle_b.sety(y - 20) #if it's safe to move, the paddle moves down by 20 pixels

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w") 
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Game loop
def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}",
                        align="center", font=("Courier", 24, "normal"))

while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Left and right (score)
    if ball.xcor() > 390:
        score_a += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle collisions
    if (340 < ball.xcor() < 350 and
        paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.dx *= -1

    if (-350 < ball.xcor() < -340 and
        paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.dx *= -1

    # Check for winner
    if score_a == 10 or score_b == 10:
        winner = "Player A" if score_a == 10 else "Player B"
        score_display.goto(0, 0)
        score_display.write(f"{winner} Wins!", align="center", font=("Courier", 36, "bold"))
        break
