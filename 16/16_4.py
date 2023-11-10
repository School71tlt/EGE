import sys
sys.setrecursionlimit(4000)

def h(x):
    if x < 3:
        return 1
    elif x > 2:
        return 2 * x - 1 + h(x - 2)

print(h(3033))