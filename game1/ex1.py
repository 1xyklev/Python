import turtle

t = turtle.Pen()
t.speed(15)  

t.reset()
for x in range(1, 5):
    t.forward(100)
    t.left(90)

turtle.done()