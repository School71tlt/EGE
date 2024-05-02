import itertools


def f(x):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))


OX = [i / 4 for i in range(6 * 4, 101 * 4 + 1)]
z = []
for a1, a2 in itertools.combinations(OX, 2):
    if all(f(x) for x in OX):
        z.append(a2 - a1)
print(min(z))
