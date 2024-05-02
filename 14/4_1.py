def f(number, base):
    result = 0
    for i, c in enumerate(reversed(number)):
        result += int(c) * base**i
    return result

for n in range(7, 100):
    print(n)
    if (f('4646', n) + f('387', n + 2)) == f('3746', n + 1):
        print("otvert", n)
        break

print(f('110', 2))
print(f('2120', 3))