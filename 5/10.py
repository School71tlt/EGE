def f(x):
    result = ''
    while x:
        result = str(x % 3) + result
        x //= 3
    return result if result else '0'


for n in range(1000):
    r = f(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + f((n % 3) * 4)
    r = int(r, 3)
    if r < 199:
        print(n)
