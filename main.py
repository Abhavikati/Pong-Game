import time
from scoreboard import Scoreboard
from turtle import Screen
from pong_ball import PongBall

from pong_paddles import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle([-350, 0])
r_paddle = Paddle([350, 0])
scoreboard = Scoreboard()
ball = PongBall()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_Is_Running = True
while game_Is_Running:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # detect collision with wall, top and bottom of screen
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # right side paddle miss
    if ball.xcor() > 375:
        ball.reset()
        scoreboard.l_point()

    # left side paddle miss
    if ball.xcor() < -375:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
