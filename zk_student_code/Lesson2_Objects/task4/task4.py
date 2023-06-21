from turtle import *
from random import randint

t = Turtle()

start = input()

while start != "0":
    for i in range(10):
        radius = randint(5, 100)
        x = randint(-200, 200)
        y = randint(-200, 200)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.circle(radius)

    start = input()