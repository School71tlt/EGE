def perevod(x, n):
    result = ''
    while x > 0:
        result = str(x % n) + result
        x = x // n
    return result

print(perevod(15, 2))
print(int('11000000', 2))
