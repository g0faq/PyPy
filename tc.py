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
size = 1
t.speed(40)
bgcolor('gray')


for a in range(3):
        for i in range(1, 180):
            colormode(255)
            if a == 0:
                t.color(sp[i])
            elif a == 1:
                t.color(sp[-i])
            else:
                t.color(sp[i])
            t.circle(size)
            t.left(5)
            size += 0.4
            bgcolor('grey')