from turtle import *

tracer(0)
left(90)
k=8

pu()
for _ in range(10):
    right(120)
    fd(10*k)
pd()
for _ in range(7):
    fd(15*k)
    right(90)
for _ in range(5):
    right(60)
    fd(20*k)
    right(30)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3)
done()


