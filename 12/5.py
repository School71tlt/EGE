maximum = float('-inf')
aba = 0
for n in range(51, 5000):
    s = '5' * n
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)
    if s.count('5') > maximum:
        maximum = s.count('5')
        aba = n
    elif s.count('5') == maximum:
        aba = min(aba, n)

print(aba)