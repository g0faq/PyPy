s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]
v = []
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            v.append(s2[j])
v.sort()
x = []
for elem in v:
    x.append(str(elem))
print(' '.join(x))