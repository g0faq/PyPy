a = input()
x = int(a)
p = ''
s = []
for i in range(1, x + 1):
    s.append(i)
for elem in s:
    p += str(elem)
    print(p)