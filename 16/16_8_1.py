# import sys
#
# sys.setrecursionlimit(2**30)
#
#
# def f(n):
#     if not n:
#         return 1
#     else:
#         return f(n - 1) * n
#
#
# print(f(400000))

a = 1

for i in range(1, 400001):
    a = (a % 1000) * i

print(a)