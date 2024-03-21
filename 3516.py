a, b = int(input()), int(input())
if a == 0 and b == 0:
    print('INF')
elif a == 0:
    print('NO')
elif (-b / a) % 2 == 0 or ((-b / a) + 1) % 2 == 0:
    print(-b // a)
else:
    print('NO')
