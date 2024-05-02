for n in range(10000):
    r = bin(n)[2:]
    c = sum(map(int, r)) % 2
    r = r + str(c)
    c = sum(map(int, r)) % 2
    r = r + str(c)
    r = int(r, 2)
    if r > 55:
        print(r)
