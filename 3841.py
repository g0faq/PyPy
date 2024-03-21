sp = input().split()
for i in range(0, len(sp) - 1, 2):
    sp[i], sp[i + 1] = sp[i + 1], sp[i]
print(*sp)