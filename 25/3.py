from fnmatch import fnmatch


def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


def p(x):
    return (div(x) == [1, x]) and (x > 1)


for n in range(0, 10 ** 10 + 1, 7777):
    if fnmatch(str(n), '12*567?'):
        d = div(n)
        if (d[0] + d[-1]) % 2 != 0:
            print(n, n / 7777)
