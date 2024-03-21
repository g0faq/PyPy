a, b, c = int(input()),int(input()), int(input())
if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
    print('NO')
else:
    print('YES')