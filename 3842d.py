sp = input().split()
s = sp[-1]
for i in range(-1, len(sp) - 1):
    sp[i] = sp[i + 1]
sp[0] = s
print(*sp)