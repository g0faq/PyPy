s = [int(a) for a in input().split()]
v = []
for elem in s:
    if elem > 0:
        v.append(str(elem))
print(len(v))