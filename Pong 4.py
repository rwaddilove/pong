# Game of Pong by Roland Waddilove
# Keep the ball in play using the bats. One or two player.
# This is just a Python learning exercise. It's not meant to be useful,
# except for others learning Python. There may be better ways to write it.
# More Python code examples at https://github.com/rwaddilove/
# Left bat = Q/A keys, right bat = Up/Down keys
# Set speed = 1 to 10, or 0 for fastest

import turtle
import random

def bat1_up() -> None:
    t1.sety(t1.ycor() + 10)

def bat1_down() -> None:
    t1.sety(t1.ycor() - 10)

def bat2_up() -> None:
    t2.sety(t2.ycor() + 10)

def bat2_down() -> None:
    t2.sety(t2.ycor() - 10)

def check_bats(ball_y):     # bat is +/- 50px from centre
    if ball_y < (t1.ycor() + 50) and ball_y > (t1.ycor() - 50): ball_dir[0] *= -1
    if ball_y < (t2.ycor() + 50) and ball_y > (t2.ycor() - 50): ball_dir[0] *= -1

# ========== M A I N =============
speed = 1                       # change this to make game faster or slower!
swidth, sheight = 400, 300      # from -swidth, -sheight <--to--> + swidth, +sheight
turtle.setup(2 * swidth + 50, 2 * sheight + 50)         # window size
turtle.Screen().screensize(2 * swidth, 2 * sheight)     # canvas size
turtle.Screen().bgcolor('red')
turtle.colormode(255)

t1 = turtle.Turtle()
t1.speed(speed)
t1.shape('square')
t1.shapesize(5.0, 1.0)  # bat is 5x20 = 100 px tall
t1.penup()
t1.setx(-swidth)

t2 = turtle.Turtle()
t2.speed(speed)
t2.shape('square')
t2.shapesize(5.0, 1.0)  # bat is 5x20 = 100 px tall
t2.penup()
t2.setx((swidth) - 10)

ball = turtle.Turtle()
ball.speed(speed)
ball.shape('circle')
ball.penup()
ball_dir = [random.choice((-2, 2)), random.choice((1, 2, 3, -1, -2, -3))]
ball.goto(0, 0)

turtle.Screen().listen()
turtle.Screen().onkeypress(bat1_up, 'q')
turtle.Screen().onkeypress(bat1_down, 'a')
turtle.Screen().onkeypress(bat2_up, 'Up')
turtle.Screen().onkeypress(bat2_down, 'Down')

turtle.tracer(0)
while -swidth < ball.xcor() < swidth:
    by = ball.ycor() + ball_dir[1]
    if abs(by) > sheight: ball_dir[1] *= -1     # bounce at top/bottom
    bx = ball.xcor() + ball_dir[0]
    ball.teleport(bx, by)
    if bx < 20 - swidth or bx > swidth - 40: check_bats(by)     # hit a bat?
    turtle.update()     # update screen

turtle.done()
