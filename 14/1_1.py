def f(n):
    s = ''
    while n > 0:
        s = str(n // 9) + s
        n //= 9
    return s
    a = f(n)


a = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338
print(a.count(not '0'))
