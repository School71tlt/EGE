damirlox = float('inf')
for n in range(4, 2000):
    s = n * '3' + '5'
    while '23' in s or '5333' in s or '33333' in s:
        if '23' in s:
            s = s.replace('23', '3', 1)
        if '5333' in s:
            s = s.replace('5333', '32', 1)
        if '33333' in s:
            s = s.replace('33333', '55', 1)
    damirlox = min(damirlox, sum(map(int, s)))
print(damirlox)
