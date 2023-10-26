import turtle
from random import seed
from random import randint

seed(1)

t = turtle.Turtle()
t.speed(4)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = turtle.Screen()

while(1==1):
    t.penup()
    t.goto(0,0)
    t.pendown()

    for i in range(360):
        screen.bgcolor("black")
        t.pencolor(colors[i % 6])
        t.forward(i)
        t.right(61)
        
    t.right(1)


turtle.done()

print("Hello World")