n = int(input())
m = int(input())
k = int(input())
c = 0
for i in range(m):
    if c < m:
        c += k // n
    else:
        break
print(c // (k // n))