from turtle import *

pen = Turtle()

def square(t, size, color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.left(90)
    t.end_fill()
    
def circle(t, radius, color):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    

def pentagon(t, size, color):
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.fd(size)
        t.left(72)
    t.end_fill()
    
start = input("square, circle, pentagon, off: ").lower()
while start != "off":
    if start == "square":
        size = int(input("Enter a length: "))
        color = input("Enter a color: ").lower()
        square(pen,size,color)
    elif start == 'circle':
        radius = int(input("Enter a radius: "))
        color = input("Enter a color: ").lower()
        circle(pen,radius,color)
    elif start == "pentagon":
        size = int(input("Enter a length: "))
        color = input("Enter a color: ").lower()
        pentagon(pen,size,color)
    else:
        print("Spelling Error, try again!")
    start = input("square, circle, pentagon, off: ").lower()

done()
