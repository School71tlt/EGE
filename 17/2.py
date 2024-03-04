cnt = 0
mx = float('-inf')
sm = 0

with open('2.txt', 'r') as f:
    lst = [int(s) for s in f]
for i in lst:
    if i % 100 == 13:
        mx = max(mx, i)

for i in range(len(lst) - 2):
    a = lst[i]
    b = lst[i + 1]
    c = lst[i + 2]
    zxc = a+b+c
    if (((a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)) or ((10 <= a <= 99) or (10 <= b <= 99) or (10 <= c <= 99))) and (zxc <= mx):
        cnt+=1
        sm +=zxc
print(cnt,sm//cnt)
