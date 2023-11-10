def f(n):
    if n > 2024:
        return n
    else:
        return n * f(n + 1)


print(f(2022) / f(2024))
