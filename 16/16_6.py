import sys
import functools

sys.setrecursionlimit(10**9)

@functools.cache
def f(n, k):
    if k == 0:
        return 0
    if k > 0 and n % k == 0:
        return f(n, k - 1) + k ** 2
    if k > 0 and n % k != 0:
        return f(n, k - 1)


print(f(11223456789, 123456789))

# хз как сделать