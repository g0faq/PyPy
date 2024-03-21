print('x y z w F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                s = str(x) + str(y) + str(z) + str(w)
                if int((x or (y and (not z))) and (not w)) == 0:
                    if s.count('1') == 2:
                        print(x, y, z, w, 0)
                else:
                    if s.count('1') == 1:
                        print(x, y, z, w, 1)