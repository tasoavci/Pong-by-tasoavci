import turtle
import time
wn = turtle.Screen()
wn.title("Pong by Taso")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.dx = 0.2

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("red")
ball.goto(0, 0)
ball.penup()
ball.dx = 0.2
ball.dy = 0.2

#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)    
#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")    
wn.onkeypress(paddle_b_down, "Down")        
#Scores
score_a = 0
score_b = 0
#Score pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align ="center",font = ("Courier", 29 , "normal"))
#Win pen
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.hideturtle()
pen2.penup()

#Main Game loop
while True:
    wn.update()
    
    
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B:{}".format(score_a,score_b), align ="center",font = ("Courier", 29 , "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1   
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B:{}".format(score_a,score_b), align ="center",font = ("Courier", 29 , "normal"))
    
    #Paddle and Ball
    if (ball.xcor() > 335 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() + -40):
        ball.setx(335)
        ball.dx *= -1
        
    if (ball.xcor() < -335 and ball.xcor() >-350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() + -40 ):
        ball.setx(-335)
        ball.dx *= -1
     
    if (score_a) == 3:
        ball.goto(0,0)
        
        pen2.goto(0,0)
        pen2.write("Player A Wins!", align ='center', font =("Courier", 50 , "normal"))
        
        
        time.sleep(3)
        pen2.clear()
        
        break
    if (score_b) == 3:
        ball.goto(0,0)
        
        pen2.goto(0,0)
        pen2.write("Player B Wins!", align ='center', font =("Courier", 50 , "normal"))
        
        
        time.sleep(3)
        pen2.clear()
        
        break