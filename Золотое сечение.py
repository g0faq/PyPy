def golden_ratio(i):
    f1 = 1
    f2 = 1
    for o in range(3, i + 2):
        la = f1
        f1 = f2
        f2 = la + f2
    print(f2 / f1)