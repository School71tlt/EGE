alphabet = [i for i in range(39)]


def f(a):
    b = 0
    for i, num in enumerate(reversed(a)):
        b += num * 39 ** i
    return b


for x in alphabet:
    for y in alphabet:
        numb = f([5, 8, x, 7, 2, 3, y, 4, 9])
        numb2 = f([y,x])
        if (numb % 38 == 0) and ((numb2**0.5) % 1 == 0) and ((numb2**0.5) != 0):
            print(numb2)