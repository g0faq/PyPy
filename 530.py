n = int(input())
m = 100
l = 100
for i in range(n):
    a = int(input())
    m += a
    if m < l:
        l = m
print(l)