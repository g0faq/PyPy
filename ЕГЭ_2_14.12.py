def F(x, y, z, w):
    return int((x and (not y)) or ((z == w) or (w and (not x))))

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if F(x, y, z, w) == 0 and w == 0:
                    print(x, y, z, w)