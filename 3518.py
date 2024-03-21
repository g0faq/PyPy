n, m, x, y = int(input()), int(input()), int(input()), int(input())
if n > m:
    if x > n // 2:
        x = n - x
    if y > m // 2:
        y = m - y

    if x > y:
        print(y)
    else:
        print(x)

if m > n:
    if x > m // 2:
        x = m - x
    if y > n // 2:
        y = n - y

    if x > y:
        print(y)
    else:
        print(x)