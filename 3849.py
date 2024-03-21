sp = [x for x in input().split()]
m = ['', 0]
for elem in sp:
    if sp.count(elem) > m[1]:
        m[0], m[1] = elem, sp.count(elem)
print(m[0])