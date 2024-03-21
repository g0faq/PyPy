s = []
v = []
x = input()
s.append(x)
while x != 0:
    s.append(x)
s = s[:-1]
for i in range(130, len(s)):
    s[i] = s[i][3:]
    v.append(str(i) + s[i])
for elem in v:
    print(elem)