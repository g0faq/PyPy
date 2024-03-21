h = [0, 8, 12, 21, 8, 17, 13, 11, 10, 20]
m = [0, 1, 15, 55, 0, 23, 47, 11, 48, 44]
a = [15, 841, 5, 10, 123, 5, 13, 190, 462, 178]
b = [23, 841, 15, 100, 456, 12, 26, 191, 381, 360]

for i in range(10):
    if h[i] == 0:
        print(480 - m[i])
    elif h[i] == 23 or h[i] == 22 and m[i] > 0:
        print(-1)
    else:
        x = (h[i] - 8) * 60 + m[i]
        if x % a[i] == 0 or x % b[i] == 0:
            print(0)
        else:
            y = min(a[i] - x % a[i], b[i] - x % b[i])
            if 480 + y > 22 * 60:
                print(-1)
            else:
                print(y)


