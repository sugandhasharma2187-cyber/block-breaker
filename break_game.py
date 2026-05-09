import time
from turtle import*
sc=Screen()
sc.setup(width=600,height=400)
sc.bgcolor("black")

paddle=Turtle()
paddle.shape("square")
paddle.color("white")
paddle.speed(0)
paddle.up()
paddle.goto(0,-180)

ball=Turtle()
ball.shape("circle")
ball.color("red")
ball.up()
ball.goto(0,0)
ball.dx=2
ball.dy=-2
bricks=[]

def left():
    if paddle.xcor()>-400:
        paddle.setx(paddle.xcor()-20)

def right():
    if paddle.xcor()<400:
        paddle.setx(paddle.xcor()+20)

sc.listen()
sc.onkey(left,"Left")
sc.onkey(right,"Right")
colors=["green","violet","blue","purple","pink"]

for row in range(4):
    for col in range(-250,300,80):
        brick=Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.up()
        brick.speed(0)
        brick.goto(col,150-(row*30))
        bricks.append(brick)

pen=Turtle()

score=0
deaths = 0
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0,170)
pen.write("score:{}".format(score),font=("arial",20),align="center")

def update_score():
    pen.clear()
    pen.write("score:{}".format(score),font=("arial",20),align="center")

# game start 
game_start = False
def start_game():
    global game_start
    game_start = True
sc.onclick(start_game)

while True:
    sc.update()
    time.sleep(0.02)
    if not game_start:
        continue

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() +ball.dy)
    # wall collision
    if ball.xcor()>290 or ball.xcor()<-290:
        ball.dx = ball.dx * -1
    
    if ball.ycor()<-290:
        deaths += 1
        ball.goto(0,0)
        ball.dy *= -1
        game_start = False
        update_score()

        if deaths == 3:
            pen.goto(0,0)
            pen.write("game over",align="center",font=("arial",30,"bold"))
            break
    
    if (-260 < ball.ycor() < -216) and (paddle.xcor()-50 < ball.xcor()< paddle.xcor() + 50):
        ball.dy *= -1
    #collision brick
    for brick in bricks:
        if brick.isvisisble() and\
         (paddle.xcor()-50 < ball.xcor() < paddle.xcor() + 50 ):
            ball.dy *= -1
            brick.hideturtle()
            bricks.remove(brick)
            score=score+10
            update_score()
         

        
        
done()
