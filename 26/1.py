with open('1.txt', 'r') as f:
    n = int(f.readline())

    a = []
    for line in f:
        a.append(list(map(int, line.split())))

time = [0]*1440

for st, end in a:
    time[st] += 1
    time[end+1] -= 1

p = 0
mx = 0
for t in time:
    p += t
    mx = max(p, mx)

cnt = 0
for t in time:
    p += t
    if p == mx:
        cnt += 1

print(cnt, mx)