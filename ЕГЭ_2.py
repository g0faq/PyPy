print('x y z')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            if int(((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))):
                print(x, y, z)