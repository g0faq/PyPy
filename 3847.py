sp = [x for x in input().split()]
res = []
for elem in sp:
    if sp.count(elem) == 1:
        res.append(elem)
print(*res)