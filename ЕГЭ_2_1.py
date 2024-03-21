print('x y z w f')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if not ((not(x and not(y)) or (not(z) or not(w))) and ((not(w) or x) or y)):
                    print(x, y, z, w, 0)

print('zywx')