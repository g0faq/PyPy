print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if int((x and (not y)) or (y == z) or (not w)) == 0:
                    print(x, y, z, w)