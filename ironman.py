import turtle

im = turtle.Turtle()
turtle.bgcolor("black")
im.color("red","red")
im.pensize(2)
#im.speed(0)

def top():
    im.begin_fill()
    im.left(20)
    im.forward(70)    
    im.right(70)
    im.forward(25)
    im.left(90)
    im.forward(25)
    im.left(70)
    im.forward(25)
    im.right(30)
    im.forward(40)
    im.left(10)
    im.forward(80)
    im.left(40)
    im.forward(50)
    im.left(10)
    im.forward(50)
    im.left(120)
    im.forward(110)
    im.right(80)
    im.forward(100)
    im.right(80)
    im.forward(110)
    im.left(120)
    im.forward(50)
    im.left(10)
    im.forward(50)
    im.left(40)
    im.forward(85)
    im.left(10)
    im.forward(40)
    im.right(30)
    im.forward(25)
    im.left(70)
    im.forward(25)
    im.left(90)
    im.forward(30)
    im.right(70)
    im.forward(68)
    im.left(20)
    im.forward(82)
    im.end_fill()
top()

def mid():
    im.begin_fill()
    im.penup()
    im.right(90)
    im.forward(10)
    im.left(30)
    im.pendown()
    im.forward(15)
    im.left(50)
    im.forward(40)
    im.left(40)
    im.forward(30)
    im.left(10)
    im.forward(20)
    im.right(10)
    im.forward(20)
    im.right(83)
    im.forward(20)
    im.right(60)
    im.forward(140)
    im.left(15)
    im.forward(30)
    im.right(30)
    im.forward(30)
    im.right(90)
    im.forward(25)
    im.left(38)
    im.forward(110)
    im.left(30)
    im.forward(30)
    im.right(70)
    im.forward(30)
    im.right(35)
    im.forward(30)
    im.left(8)
    im.forward(142)
    im.right(65)
    im.forward(21)
    im.right(90)
    im.forward(25)
    im.left(20)
    im.forward(50)
    im.left(35)
    im.forward(35)
    im.left(35)
    im.forward(20)
    im.right(48)
    im.forward(75)
    im.end_fill()
mid()

def bottom():
    im.begin_fill()
    im.penup()
    im.right(90)
    im.forward(180)
    im.left(90)
    im.pendown()
    im.forward(20)
    im.right(40) 
    im.forward(32)
    im.left(95)
    im.forward(38) 
    im.right(103)
    im.forward(27)
    im.right(78) 
    im.forward(60) 
    im.right(90)
    im.forward(35) 
    im.left(40) 
    im.forward(20) 
    im.right(35) 
    im.forward(15) 
    im.left(31) 
    im.forward(50)
    im.left(31)
    im.forward(15)
    im.right(35)
    im.forward(20)
    im.left(40)
    im.forward(35)
    im.right(90) 
    im.forward(60)
    im.right(78)
    im.forward(22)
    im.right(87)
    im.forward(38)
    im.left(70)
    im.forward(33)
    im.right(31)
    im.forward(86)
    im.right(90)
    im.forward(10)
    im.end_fill()
bottom()

turtle.done()