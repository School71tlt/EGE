import sys
import functools

sys.setrecursionlimit(10 ** 9)


@functools.cache
def f(n):
    # print(f'f({n})')
    if n <= 2:
        return 1
    if n > 2 and n % 2 == 1:
        return f(n - 1) - n
    if n > 2 and n % 2 == 0:
        return f(n - 2) + g(n - 1) + 2


@functools.cache
def g(n):
    # print(f'g({n})')
    if n <= 0:
        return 2
    if n > 0 and n % 2 == 1:
        return f(n - 1) - 2 * g(n - 2)
    if n > 0 and n % 2 == 0:
        return 2 * f(n - 2) - 2 * g(n - 1)


print(f(96))
