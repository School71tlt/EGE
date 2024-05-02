sp = []
def p3(x):
    result = ''
    while x:
        result = str(x % 3) + result
        x = x // 3
    return result if result else '0'


for n in range(10000):
    r = p3(n)
    if sum(map(int, r)) % 4 == 0:
        r = '1' + r[:-2]
    else:
        r = r + p3((sum(map(int, r)) % 4) * 3)
    r = int(r, 3)
    if r > 353:
        sp.append(r)
print(min(sp))
