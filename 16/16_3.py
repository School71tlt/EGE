import sys

sys.setrecursionlimit(10000)


def f(n):
    if n >= 3210:
        return 1
    else:
        return f(n + 3) + 7


def g(n):
    if n < 10:
        return n
    else:
        return g(n - 3) + 5


print(f(15) - g(3000))
