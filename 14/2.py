f = 81**18-(81**8-1)*((8+1)**8+1)/8-8
count = 0
while f:
    if f % 3 == 1:
        count +=1
    f = f // 3

print(count)
