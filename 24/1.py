with open('1.txt', 'r') as f:
    s = '!' + f.readline()

curr = 0
mx = 0
for i in range(len(s)-1):
    a = s[i-1]
    b = s[i]
    if b in 'VWXYZ':
        if a + b in 'VWXYZV':
            curr += 1
        else:
            curr = 1
    else:
        curr = 0
    mx = max(mx, curr)
print(mx)