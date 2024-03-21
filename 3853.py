sp = input().split()
k = int(input())
r = sp[-1]
for i in range(len(sp) - 1, 0, -1):
    sp[i] = sp[i - k]
sp[0] = r
print(*sp)