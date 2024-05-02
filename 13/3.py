s = ''
for i in [203, 111, 195, 0]:
    s += (bin(i)[2:] + '.').zfill(9)

print(s)

s = ''
for i in [255, 255, 240, 0]:
    s += (bin(i)[2:] + '.').zfill(9)

print(s)