s = [int(x) for x in input().split()]
a = s[0]
b = s[1]
if a < b:
    print(a // 2 + a % 2, a)
if b < a:
    print(a // 2 + a % 2, b)