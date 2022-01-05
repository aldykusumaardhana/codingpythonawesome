import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(100)

color = ["red", "yellow", "green", "blue", "purple"]

for i in range(5):
    
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    
    t.penup()
    t.goto(x,y)
    t.pendown()
    
    size = random.randint(10,200)
    i = random.randint(0,4)
    
    t.color(color[i])
    
    for i in range(36):
        t.forward(size)
        t.backward(size)
        t.left(10)