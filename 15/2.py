def f(x, y):
    return ((3 * x + y) > 48) or (x > y) or ((4 * x + y) < a)


for a in range(-10000, 10000):
    if any(f(x, y) == 0 for x in range(1000) for y in range(1000)):
        print(a)
