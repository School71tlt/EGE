cnt = 0
mx = float('-inf')

with open('1.txt', 'r') as f:
    lst = [int(s) for s in f]
    print(lst)
    for i in range(len(lst)-1):
        if (lst[i] % 3 == 0) or (lst[i+1] % 3 == 0):
            cnt += 1
        mx = max(mx, lst[i] + lst[i+1])

print(mx, cnt)
