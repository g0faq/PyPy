def NOD(x, y):
    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return x + y


print(NOD(int(input()), int(input())))