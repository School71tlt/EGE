from turtle import *
color('blue', 'pink')
begin_fill()
right(90)
for _ in range(3):
    right(45)
    forward(10)
    right(45)
right(315)
forward(10)
for _ in range(2):
    right(90)
    forward(10)
end_fill()
canvas = getcanvas()
cnt = 0
for y in range(-100, 100):
    for x in range(-100, 100):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            cnt+=1

print(cnt)
done()
exit()