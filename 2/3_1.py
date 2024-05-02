print('x y z w ')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x <= y) or (not w == z)) == ((x <= y) == (w and not z)):
                    print(x, y, z, w)
