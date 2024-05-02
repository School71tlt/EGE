from itertools import *


def f(x, y, z, w):
    return (x and (not z)) or (y == z) or (not w)

for a1,a2,a3,a4 in product([0,1], repeat = 4):
    table = [(a1,a2,0,0),(1,0,a3,0),(1,0,1,a4)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,row)))for row in table] == [0,0,0]:
                print(p)