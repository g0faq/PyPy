s = input()
x = []
for i in range(len(s)):
    if s[i] == '1':
        x.append('one')
    else:
        x.append(s[i])
for elem in x:
    print(elem, end='')