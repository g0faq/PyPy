a, b, n = int(input()), int(input()), int(input())
x, y = 0, 0
nod_ab = 0

for i in range(1, max(a, b)):
    if a % i == 0 and b % i == 0:
        nod_ab = i

if (a % 2 == 0 and b % 2 == 0 and n % 2 != 0) or (n > a and n > b) or (n % nod_ab != 0) or (a == b != n):
    print('Impossible')
else:
    if a == n:
        print('>A')
    elif b == n:
        print('>B')
    else:
        while x != n or y != n:
            if a < b:
                print('>A')
                x = a
                if x == n or y == n:
                    break

                print('A>B')
                if x + y > b:
                    x -= b - y
                    y = b
                    if x == n or y == n:
                        break

                    print('B>')
                    y = 0

                    print('A>B')
                    x, y = 0, x
                else:
                    y += x
                    x = 0
                    if x == n or y == n:
                        break
            else:
                print('>B')
                x = b
                if x == n or y == n:
                    break

                print('B>A')
                if x + y > a:
                    x -= a - y
                    y = a
                    if x == n or y == n:
                        break

                    print('A>')
                    y = 0

                    print('B>A')
                    x, y = 0, x
                else:
                    y += x
                    x = 0
                    if x == n or y == n:
                        break