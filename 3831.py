s = [int(x) for x in input().split()]
v = []
for i in range(len(s)):
    if s[i] > s[i - 1]:
        v.append(str(s[i]))
if len(v) > 1:
    print(' '.join(v))
elif len(v) == 1:
    print(v[0])