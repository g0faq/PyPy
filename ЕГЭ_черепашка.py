import turtle

t = turtle.Turtle()
t.down()
t.left(90)
for _ in range(4):
    t.forward(100)
    t.right(270)
t.up()
for _ in range(3):
    t.right(270)
    t.forward(50)
    t.right(90)
t.down()
for _ in range(2):
    t.forward(100)
    t.right(270)
    t.forward(120)
    t.right(270)