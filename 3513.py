x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (abs(x2 - x1) == 2 and abs(y2 - y1) == 1) or (abs(y2 - y1) == 2 and abs(x2 - x1) == 1):
    print('YES')
else:
    print('NO')