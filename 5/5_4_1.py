spisemax = []
for n in range(1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'
    if r.count('1') % 2 == 1:
        r = r + '1'
    else:
        r = r + '0'
    r = int(r, 2)
    if r > 2023:
        spisemax.append(r)
print(min(spisemax))
