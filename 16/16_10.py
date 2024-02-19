import sys
import functools

sys.setrecursionlimit(10 ** 9)


@functools.cache
def f(n):
    print(f'f({n})')
    if n <= 1:
        return n
    if n > 1 and n % 3 == 0:
        return n + f(n / 3)
    if n > 1 and n % 3 != 0:
        return n + f(n + 3)
    if n > 4000:
        return None


for n in range(3, 1000):
    print(n)
    if f(n) == None:
        pass
    elif f(n) > 100:
        print(n)

# потом доделаем