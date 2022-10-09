from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.collide()
    elif ball.xcor() > 380:
        ball.reset()
        score.l_point()
    elif ball.xcor() < -390:
        ball.reset()
        score.r_point()
    elif score.check_point() == 1:
        ball.hideturtle()
        ball.goto(0, 0)
        screen.tracer(1)
        score.l_message()
        screen.update()
        game_is_on = False
    elif score.check_point() == 0:
        ball.hideturtle()
        ball.goto(0, 0)
        screen.tracer(1)
        score.r_message()
        screen.update()
        game_is_on = False

screen.exitonclick()
