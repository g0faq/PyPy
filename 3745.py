s = input()
x = [] 
for i in range(len(s)):
    if s[i] != '@':
        x.append(s[i])
for elem in x:
    print(elem, end='')