def f(x, end):
    if x == end:
        return 1
    if x > end or x == 16:
        return 0
    return f(x + 1, end) + f(x + 3, end) + f(x ** 2, end)


print(f(3, 20) * f(20, 26))
