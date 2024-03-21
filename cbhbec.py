n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
a1 = (a // b) * (b // a)
a2 = (a // c) * (c // a)
a3 = (a // d) * (d // a)
b1 = (b // c) * (c // b)
b2 = (b // d) * (d // b)
c1 = (c // d) * (d // c)
print(a1 + a2 + a3 + b1 + b2 + c1)