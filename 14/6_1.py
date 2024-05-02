def pereveod(x):
    result = []
    while x:
        result = [x % 6] + result
        x = x // 6
    return result


a = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
b = pereveod(a)
print(b.count(5) - b.count(0))
