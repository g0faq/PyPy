f = open('24 (1).txt')
s = f.readline()
x1, x2 = 'AO', 'CDF'
f = False
count = 0
m = 0
i = 0
while i < len(s):
    if s[i] in x2 and s[i + 1] in x1:
        f = True
    else:
        f = False
        m = max(m, count)
        count = 0
    if f:
        count += 1
    i += 2

print(m)