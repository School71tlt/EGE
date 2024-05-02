from fnmatch import fnmatch

for n in range(0, 10 ** 10, 2024):
    if fnmatch(str(n), '1?2*4') and (n ** 0.5) % 1 == 0:
        print(n, n / 2024)
