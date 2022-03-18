import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# New right paddle 
r_paddle = Paddle(350, 0)
# New left paddle
l_paddle = Paddle(-350, 0)
# New ball 
ball = Ball()
# New scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    # Update the entire screen 
    screen.update()
    ball.move()

    #Detect collision with wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()
    
    # Detect collision with the left paddle 
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()
    
    #Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position_rloses()
        scoreboard.increase_left()
    
    #Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position_lloses()
        scoreboard.increase_right()

    if scoreboard.lscore == 11:
        game_is_on = False
        scoreboard.goto(0,0)
        scoreboard.write("The left player won", align="center", font=("Courier", 40, "normal"))
    
    if scoreboard.rscore == 11:
        game_is_on = False
        scoreboard.goto(0,0)
        scoreboard.write("The right player won", align="center", font=("Courier", 40, "normal"))



screen.exitonclick()