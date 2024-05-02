from itertools import *


def f(x, y, z, w):
    return ((w or y) and (x <= (not z))) and not w


d = set()
for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(a1, 0, a2, 0), (1, a3, a4, a5), (1, 1, 0, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                d.add(p)

print(len(d))
