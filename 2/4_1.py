print('w x y z F')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(w, x, y, z, int(((x <= y) or (z <= w)) and not (x <= w)))
