def f(x):
    a = []
    while x:
        a = [x % 16] + a
        x //=16
    return a

s = '1' + 105 * '0'
while '10' in s:
    if '100' in s:
        s = s.replace('100', '1011',1)
    else:
        s = s.replace('10','11',1)
s = sum(f(int(s,2)))
print(s)

