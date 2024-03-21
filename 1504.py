a, b, c = map(int, input().split())
if a == 0:
    if b == 0 and c == 0:
        print(-1)
    elif b == 0:
        print('0')
    else:
        print(f'1 {-c / b:.2f}')
else:
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1, x2 = (-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)
        if x2 < x1:
            print(f'2 {x2:.2f} {x1:.2f}')
        else:
            print(f'2 {x1:.2f} {x2:.2f}')
    elif D == 0:
        print(f'3 {-b / (2 * a):.2f}')
    else:
        print(0)
