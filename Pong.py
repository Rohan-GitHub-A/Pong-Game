import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @Rohan Kumar")
wn.bgpic("forest_mountains_sunset_cool_weather_minimalism.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("#63c894")
paddle_a.penup()
paddle_a.goto(-350 , 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("#63c894")
paddle_b.penup()
paddle_b.goto(350 , 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#c60a65")
ball.penup()
ball.goto(0 , 0)
ball.dx = 0.15
ball.dy = 0.15

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0 , 260)
pen.write("Player-A:0   Player-B:0" , align="center" , font=("Courier" , 20, "bold"))

#Functions For Paddle A:
def paddle_a_up():
    y = paddle_a.ycor()
    y += 15
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 15
    paddle_a.sety(y)

#Functions For Paddle B:
def paddle_b_up():
    y = paddle_b.ycor()
    y += 15
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 15
    paddle_b.sety(y)

#KeyBoard Binding:
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.listen()
wn.onkeypress(paddle_a_down, "s")

wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.listen()
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC | winsound.SND_NOWAIT)


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC | winsound.SND_NOWAIT)


    if ball.xcor() > 390:   
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player-A:{}   Player-B:{}".format(score_a , score_b) , align="center" , font=("Courier" , 20, "bold"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player-A:{}   Player-B:{}".format(score_a , score_b) , align="center" , font=("Courier" , 20, "bold"))

    # Paddle And Ball Collision
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
    
