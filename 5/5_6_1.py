count = 0
for n in range(10000):
    r = oct(n)[2:]
    if n % 7 == 0:
        r = r + r[-2:]
    else:
        r = r + oct((n % 7) * 7)[2:]
    r = int(r, 8)
    print(r)
    if r < 3000:
        count += 1
print(count)
