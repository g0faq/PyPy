n = int(input())
a = int(input())
b = int(input())
c = int(input())
x = c * 3 + b * 2 + a + 1
y = x - (a + b + c)
if y > n:
    print(n)
else:
    print(y)
