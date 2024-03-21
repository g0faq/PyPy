s = input()
f1 = s.find('h')
f2 = s.rfind('h')
x = []
for i in range(len(s)):
    if i == f1 or i == f2:
        x.append(s[i])
    elif s[i] == 'h':
        x.append('H')
    else:
        x.append(s[i])
for elem in x:
    print(elem, end='')