from turtle import *
pencil = Turtle()

color_choices = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(len(color_choices)):
    pencil.color(color_choices[i]) 
    pencil.width(5) 
    pencil.forward(100)
    pencil.right(60)
done()