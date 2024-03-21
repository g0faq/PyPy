from turtle import *

sp = [0] * 180
for i in range(45):
    sp[i] = (round(255 - (i * 2.55)), 0, 0)
for i in range(45):
    sp[i + 45] = (round(127.5 - (i * 2.55)), 0, round((i * 2.55)))
for i in range(45):
    sp[i + 90] = (0, round(i * 2.55), round(127.5 - (i * 2.55)))
for i in range(45):
    sp[i + 135] = (0, round(127.5 + (i * 2.55)), 0)

t = Turtle()
t.speed(50)
bgcolor('gray')

for i in range(180):
    t.pensize(3)
    colormode(255)
    t.color(sp[i])
    t.forward(300)
    t.right(30)
    t.forward(2)
    t.left(60)
    t.forward(50)
    t.right(30)

    t.penup()
    t.setposition(0, 0)
    t.pendown()
    t.right(2)