s = input()
x = []
f1 = s.find('h')
f2 = s.rfind('h') 
x.append(s[:f2])
x.append(s[f1 + 1:])
for elem in x:
    print(elem, end='')