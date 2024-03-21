a, b, c = int(input()), int(input()), int(input())
if c < a:
    a, c = c, a
elif c < b:
    b, c = c, b

if c ** 2 == a ** 2 + b ** 2:
    print('rectangular')
elif c ** 2 < a ** 2 + b ** 2:
    print('acute')
elif c ** 2 > a ** 2 + b ** 2:
    print('obtuse')
else:
    print('impossible')