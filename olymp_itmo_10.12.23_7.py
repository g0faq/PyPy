def F1(x1, x2, x3, x4):
    return int(((not x1) and x2 or x1 and (not x2)) or (not x1) and (not x2))


def F2(x1, x2, x3, x4):
    return int((x1 and (not x2) or (not x1) and x2) and (x3 and x4))


def F3(x1, x2, x3, x4):
    return int(((not x3) and x4 or x3 and (not x4)) or (not x3) and (not x4))


def F4(x1, x2, x3, x4):
    return int((x1 and x2) and (x3 and (not x4) or (not x3) and x4))


for x1 in (0, 1):
    for x2 in (0, 1):
        for x3 in (0, 1):
            for x4 in (0, 1):
                if int(F1(x1, x2, x3, x4) or F2(x1, x2, x3, x4) or F3(x1, x2, x3, x4) or F4(x1, x2, x3, x4)) == 0:
                    print(x1, x2, x3, x4)