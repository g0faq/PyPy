s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]
c = 0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            c += 1
print(c)