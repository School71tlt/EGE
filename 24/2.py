with open('2.txt', 'r') as f:
    s = '!' + f.readline()

curr = 0
mx = 0
damirlox = ''

for i in range(len(s)):
    a = s[i - 1]
    b = s[i]
    if b in 'RSQ':
        if a + b in 'RSQR':
            curr += 1
            damirlox += b
        else:
            curr = 1
            damirlox = b
    else:
        curr = 0
        damirlox = 0
    mx = max(curr,mx)

print(mx)
