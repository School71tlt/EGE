print('w x y z F')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not ((x and not y) or (y == z) or not w):
                    print(w, x, y, z, 0)
