def perevod_v_3(x):
    result = ''
    while x > 0:
        result = str(x % 3) + result
        x = x // 3
    return result

some_list = []

for n in range(10000):
    result = perevod_v_3(n)
    if n % 4 == 0:
        result += result[-3:]
    else:
        result += perevod_v_3((n % 4) * 4)
    if result != '':
        i = int(result, 3)
    else:
        i = 0
    if i < 127:
        print(i)
        some_list.append(i)

print('max - ',max(some_list))