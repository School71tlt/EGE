def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    return f(x + d, end) + f(x * 2, end)


k = 0
for d in range(1,50):
    k = f(1, 10) * f(10, 100)
    if k == 13:
        print(d)
