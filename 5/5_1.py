some_list = []
for n in range(1, 500):
    s = bin(n)[2:]
    if n % 3 == 0:
        s += s[-3:]
    else:
        s = s + bin((n % 3) * 3)[2:]
    r = int(s, 2)
    if r > 151:
        some_list.append(r)
print(min(some_list))

