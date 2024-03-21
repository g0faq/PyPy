sp = input().split()
r = sp[-1]
for i in range(len(sp) - 1, 0, -1):
    sp[i] = sp[i - 1]
sp[0] = r
print(*sp)