with open('5.txt') as f:
    s = f.readline()

left = m = k = 0
for r in range(1, len(s)):
    if r >= 2 and (s[r - 2] + s[r - 1] + s[r] in ['ROR', 'ORO']):
        k = 0
        left = r - 1
    if s[r-1] + s[r] == 'RO':
        k += 1
    while k > 21:
        if s[left] + s[left+1] == 'RO':
            k -= 1
        left += 1
    if k == 21:
        m = max(m, r-left+1)

print(m)