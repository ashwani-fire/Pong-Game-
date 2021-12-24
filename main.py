from paddle import paddle
from score import score
from ball import ball
from turtle import Turtle,Screen
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


Ball = ball()
Score = score()
r_paddle = paddle((350,0))
l_paddle = paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    Ball.move()
    if Ball.xcor()>380:
        Score.l_point()
        Ball.reset_ball()
    
    if Ball.xcor()<-380:
        Score.r_point()
        Ball.reset_ball()
     
    if Ball.ycor()>280 or Ball.ycor()<-280:
        Ball.bounce_y()
    
    if Ball.distance(r_paddle) < 50 and Ball.xcor() > 320 or Ball.distance(l_paddle) < 50 and Ball.xcor() < -320:
        Ball.bounce_x()            
            
        
screen.exitonclick()        
    
