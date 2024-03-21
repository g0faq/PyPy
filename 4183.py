sp = [int(x) for x in input().split()]
a = (sp[0], sp[1])
b = (sp[2], sp[3])


def NOD(x, y):
    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return (x, y)


