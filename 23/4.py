def f2(x):
    r = bin(x)[2:]
    r += bin(x % 5)[2:]
    r = int(r, 2)
    return r


def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    return f(x + 1, end) + f(f2(x), end)


print(f(1, int('101000101', 2)))
