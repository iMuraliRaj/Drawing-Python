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

t.color("black")
t.backward(140)
t.right(90)
t.forward(400)
t.left(90)
t.forward(70)
t.color("green")
t.begin_fill()
t.backward(140)
t.left(90)
t.forward(400)
t.right(90)
t.forward(70)
t.right(90)
t.forward(400)
t.end_fill()

t.penup()
t.goto(0, -39)
t.pendown()
r = 35
t.color("blue")
t.circle(r)

t.left(90)
t.forward(70)
t.backward(35)
t.right(90)


turtle.done()
