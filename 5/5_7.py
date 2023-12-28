for n in range(10000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + '010'
    else:
        r = r + bin(5 * (n % 3))[2:]
    r = int(r, 2)
    if r % 2 == 0 and r > 300:
        print(n, r)
