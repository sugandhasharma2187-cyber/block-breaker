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
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0,170)
pen.write("score:{}".format(score),font=("arial",20))
done()