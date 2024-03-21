sp = [int(x) for x in input().split()]
for i in range(len(sp) - 1):
    for j in range(len(sp) - i - 1):
        if sp[j] == 0 and sp[j + 1] != 0:
            sp[j], sp[j + 1] = sp[j + 1], sp[j]

print(*sp)