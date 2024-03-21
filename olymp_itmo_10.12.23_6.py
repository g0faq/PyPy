def F(a, b, c, d, e, f):
    return int(((((((not a) and (not b)) == c) <= (not c)) <= ((((not b) and (not c)) == d) <= (not d))) <= ((((not c) and (not d)) == e) <= (not e))) <= ((((not d) and (not e)) == f) <= (not f)))


print('d e f F')
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            for d in (0, 1):
                for e in (0, 1):
                    for f in (0, 1):
                        x = F(a, b, c, d, e, f)
                        if x == 0:
                            print(d, e, f, x)
                        if int(d or e or not f) == 0:
                            print(d, e, f, 0)