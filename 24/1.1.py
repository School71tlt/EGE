with open('1.txt', 'r') as f:
    s = f.readline().replace('T', '!').replace('U', '!')

for x in 'VWXYZ':
    for y in 'VWXYZ':
        if x + y not in 'VWXYZV':
            while x + y in s:
                s = s.replace(x + y, x + '!' + y)

print(max(map(len, s.split('!'))))