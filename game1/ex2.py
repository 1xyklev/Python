import turtle

t = turtle.Pen()
t.speed(10)  

t.reset()
for x in range(1, 38):
    t.forward(100)
    t.left(175)

turtle.done()