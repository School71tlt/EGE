xyi = 0
for n in range(4, 10000):
    s = '3' + n * '5'
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)
    xyi = max(xyi, sum(map(int, s)))
print(xyi)
