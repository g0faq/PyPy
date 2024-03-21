from turtle import *

t = Turtle()
t.speed(5)
bgcolor('gray')

t.penup()
t.setpos(-500, -300)
pendown()
t.pensize(2)

for i in range(200):
    colormode(255)
    t.pencolor(255, 0, 0)
    t.fd(10)
    t.right(5)
    t.left(10)
