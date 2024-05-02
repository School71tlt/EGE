for n in range(10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '01'
    if n % 2 != 0:
        r = '1' + r + '1'
    r = int(r, 2)
    if r > 156:
        print(n)
