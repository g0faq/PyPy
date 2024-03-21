s = input()
x = []
f1 = s.find('h')
f2 = s.rfind('h')
x.append(s[:f1 + 1])
a = s[f1:f2]
x.append(a[::-1])
x.append(s[f2 + 1:])
for elem in x:
    print(elem, end='')