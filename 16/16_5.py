from functools import cache


@cache
def f(n):
    if n < 10:
        return n
    else:
        return f(n % 10) + f(n // 10)


for n in range(2 ** 63):
    print(n)
    if f(n) == 159:
        print('dfhdgjkh')

# хз, как сделать
