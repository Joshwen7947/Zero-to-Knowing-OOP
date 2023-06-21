from turtle import *
from random import randint

pen = Turtle()

for i in range(4):
    # Generate random color
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r/255, g/255, b/255)  

    # Generate random location
    x = randint(-200, 200)  
    y = randint(-200, 200)  

    # Move to the random location
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # Draw the square with the random color
    pen.color(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(100)
        pen.right(90)
    pen.end_fill()

done()
