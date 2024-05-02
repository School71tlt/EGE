from turtle import *
tracer(0)
screensize(10000,100000)
left(90)
pensize(1)
pu()
k = 40
for i in range(10):
    right(120)
    forward(10*k)
pendown()
for i in range(7):
    forward(15*k)
    right(90)
for i in range(5):
    right(60)
    forward(20*k)
    right(30)

pu()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot(5)
update()
exitonclick()
done()