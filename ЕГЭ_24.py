f = open('24.txt')
s = f.readline()
s2 = 'XZZY'


res = []

for i in range(s.count(s2) + 100):
    res.append(s[s.find(s2) + 1:].find(s2) - s.find(s2) + 8)
    s = s[s[s.find(s2) + 1:].find(s2) + 4:]

print(max(res))



f = open('24_1205.txt')
s = f.readline()
count = 0
m = 0
for elem in s:
    if elem != 'G' and elem != 'W' and elem != 'P':
        count += 1
        if count > m:
            m = count
    else:
        count = 0

print(m)