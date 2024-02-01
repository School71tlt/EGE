alph = '0123456789ABCDEFGHIJK'

for x in alph:
    for y in alph:
        f = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
        if f % 18 != 0:
            break
    else:
        print(x)

f = (int(f'12{5}{3}9', 21) + int(f'36{5}99', 21)) / 18
print(f)