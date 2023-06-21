from turtle import *

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

def triangle(t, color):
    t.color(color)
    t.begin_fill()
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()
    
t = [t1,t2,t3,t4]
y = 100
for i in t:
    i.penup()
    i.goto(0,y)
    i.pendown()
    y -= 100

triangle(t1,"blue")
triangle(t2,"red")
triangle(t3,"orange")
triangle(t4,"green")

done()