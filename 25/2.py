from fnmatch import fnmatch

for n in range(0, 10 ** 10, 1234):
    if fnmatch(str(n), '4*5*6') and fnmatch(str(n), '?74*68?'):
        print(n, n // 1234)
