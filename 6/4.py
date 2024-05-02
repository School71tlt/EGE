from turtle import *

tracer(0)
left(90)
k = 15
for _ in range(2):
    fd(10 * k)
    right(90)
    fd(18 * k)
    right(90)
pu()
fd(5 * k)
right(90)
fd(14 * k)
left(90)
pd()
for _ in range(2):
    fd(17 * k)
    right(90)
    fd(7 * k)
    right(90)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x * k,y* k)
        dot(5)
done()

