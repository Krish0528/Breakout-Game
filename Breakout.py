from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

b_paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()

tx, ty = -300, 200
bricks = []
for _ in range(6):
    for _ in range(12):
        brick = Brick(tx, ty)
        bricks.append(brick)
        tx += 55
    ty -= 25
    tx = -300

screen.listen()
screen.onkey(b_paddle.go_left, "Left")
screen.onkey(b_paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < -300:
        ball.reset_position()

    if ball.distance(b_paddle) < 70 and ball.ycor() < -220:
        ball.bounce_y()

    if (scoreboard.score / 10) == len(bricks):
        time.sleep(5)
        exit()

    if ball.ycor() >= 50:
        for brick in bricks:
            if not brick.white:
                if ball.ycor() >= brick.ycor() - 25:
                    if ball.xcor() >= brick.xcor() - 25:
                        if ball.xcor() <= brick.xcor() + 25:
                            ball.bounce_y()
                            brick.color('black')
                            scoreboard.increase_score()
                            brick.white = True
                            break

screen.exitonclick()
