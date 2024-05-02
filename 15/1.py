def de(n, m, k):
    mx = 0
    for i in range(1, min(n, m) + 1):
        if ((n % i) == 0) and ((m % i) == 0):
            mx = max(mx, i)
    return mx == k


def f(x):
    return de(a, 420, 2) or ((not de(a, x, 12)) <= (not de(110, x, 11)))


cnt = 0
for a in range(1, 1001):
    if all(f(x) for x in range(1000)):
        cnt += 1

print(cnt)
