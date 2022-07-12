import fnmatch
import turtle
from turtle import *

# screen for output
screen = turtle.Screen()

# Defining a turtle Instance
t = turtle.Turtle()
speed(5)

# initially penup()
t.penup()
t.goto(-200, 100)
t.pendown()

t.color("orange")
t.begin_fill()

t.forward(400)
t.right(90)
t.forward(70)
t.right(90)
t.forward(400)
t.right(90)
t.forward(70)
t.end_fill()



turtle.done()
