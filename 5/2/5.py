print('a b c F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            print(a, b, c, ((a and c) or (not a and (b or not c))))
