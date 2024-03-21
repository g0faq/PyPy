s = [int(x) for x in input().split()]
v = []
for elem in s:
    if elem % 2 != 0 and elem != 0:
        v.append(str(elem))
if len(v) > 0:
    print(min(v))
else:
    print(0)