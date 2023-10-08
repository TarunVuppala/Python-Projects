import turtle
import time
#screen
s=turtle.Screen()
s.title("FLAPPY BIRD")
s.bgcolor("blue")
s.bgpic("1.gif")
s.setup(width=800,height=500)
s.tracer(0)
#register shape
s.register_shape("bir.gif")
#bird object
pen=turtle.Turtle()
pen.speed(0)
pen.penup
pen.color("white")
pen.write("Score: 0",align="left",font=("Arial",32,"normal"))
pen.hideturtle()

#bird
b=turtle.Turtle()
b.speed(0)
b.penup()
b.color("yellow")
b.shape("bir.gif")
b.goto(-200,0)
b.dx=0
b.dy=1
#pipes
p1_top=turtle.Turtle()
p1_top.speed(0)
p1_top.penup()
p1_top.color("green")
p1_top.shape("square")
p1_top.shapesize(stretch_wid=18,stretch_len=3,outline=None)
p1_top.goto(300,250)
p1_top.dx=-2
p1_top.dy=0
p1_top.value=1

p1_bottom=turtle.Turtle()
p1_bottom.speed(0)
p1_bottom.penup()
p1_bottom.color("green")
p1_bottom.shape("square")
p1_bottom.shapesize(stretch_wid=18,stretch_len=3,outline=None)
p1_bottom.goto(300,-250)
p1_bottom.dx=-2
p1_bottom.dy=0

p2_top=turtle.Turtle()
p2_top.speed(0)
p2_top.penup()
p2_top.color("green")
p2_top.shape("square")
p2_top.shapesize(stretch_wid=16,stretch_len=3,outline=None)
p2_top.goto(600,280)
p2_top.dx=-2
p2_top.dy=0
p2_top.value=1

p2_bottom=turtle.Turtle()
p2_bottom.speed(0)
p2_bottom.penup()
p2_bottom.color("green")
p2_bottom.shape("square")
p2_bottom.shapesize(stretch_wid=16,stretch_len=3,outline=None)
p2_bottom.goto(600,-280)
p2_bottom.dx=-2
p2_bottom.dy=0

gravity=-0.3

def go_up():
    b.dy+=8
    if b.dy>8:
        b.dy=8
#functioning key
s.listen()
s.onkeypress(go_up,"space")
#score
b.score=0
pipes=[(p1_top,p1_bottom),(p2_top,p2_bottom)]
#loop
while True:
    time.sleep(0.02)
    s.update()
    b.dy+=gravity
    #moving player
    y=b.ycor()
    y+=b.dy
    b.sety(y)

    if b.ycor()<-390:
        b.dy=0
        b.sety(-390)
    
    for pipe_pair in pipes:
        pipe_top=pipe_pair[0]
        pipe_bottom=pipe_pair[1]
        x=p1_top.xcor()
        x+=p1_top.dx
        p1_top.setx(x)
    
        x=p1_bottom.xcor()
        x+=p1_bottom.dx
        p1_bottom.setx(x)

        if p1_top.xcor()<-350:
            p1_top.setx(600)
            p1_bottom.setx(600)
            p1_top.value=1
        x=p2_top.xcor()
        x+=p2_top.dx
        p2_top.setx(x)

        x=p2_bottom.xcor()
        x+=p2_bottom.dx
        p2_bottom.setx(x)

        if p2_top.xcor()<-350:
            p2_top.setx(350)
            p2_bottom.setx(350)
            p2_top.value=1
        if (b.xcor()+20>pipe_top.xcor()-20) and (b.xcor()-20<pipe_top.xcor()+20):
            if (b.ycor()+30>pipe_top.ycor()-160) or (b.ycor()-30<pipe_bottom.ycor()+160):
                pen.clear()
                pen.write("Game Over",move=False, align="center",font=("Arial",32,"normal"))
                s.update()
                time.sleep(3)
                b.score=0
                p1_top.setx(300)
                p1_bottom.setx(300)
                p1_top.setx(300)
                p1_bottom.setx(300)
                b.goto(-200,0)
                b.dy=0
                pen.clear()
                pen.write("Score: 0",align="left",font=("Arial",32,"normal"))
    
        if pipe_top.xcor()+30<b.xcor()-10:
            b.score+=pipe_top.value
            pipe_top.value=0
            pen.clear()
            pen.write(b.score,move=False,align="center",font=("Arial",32,"normal"))

        if (b.xcor()+20>pipe_top.xcor()-20) and (b.xcor()-20<pipe_top.xcor()+20):
            if (b.ycor()+20>pipe_top.ycor()-160) or (b.ycor()-20<pipe_bottom.ycor()+160):
                pen.clear()
                pen.write("Game Over",move=False, align="center",font=("Arial",32,"normal"))
                s.update()
                time.sleep(3)
                b.score=0
                p2_top.setx(300)
                p2_bottom.setx(300)
                p2_top.setx(300)
                p2_bottom.setx(300)
                b.goto(-200,0)
                b.dy=0
                pen.clear()
                pen.write("Score: 0",align="left",font=("Arial",32,"normal"))
    
        if pipe_top.xcor()+30<b.xcor()-10:
            b.score+=pipe_top.value
            pipe_top.value=0
            pen.clear()
            pen.write(b.score,move=False,align="center",font=("Arial",32,"normal"))

s.mainloop()