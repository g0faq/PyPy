n = int(input())
m = n
c1, с5, c10, с20, c60 = 0, 0, 0, 0, 0
c60 = n // 60
n %= 60
c20 = n // 20
n %= 20
c10 = n // 10
n %= 10
c5 = n // 5
n %= 5
c1 += n
if m % 60 > 36:
    c60 += 1
    c20 = 0
    c10 = 0
    c5 = 0
    c1 = 0
print(c1, c5, c10, c20, c60)