'''f = open('17.txt')
sp = [int(x) for x in f]

count = 0
sr = 0
for elem in sp:
    if elem % 2 == 0:
        count += 1
        sr += elem
sr /= count

count = 0
ma = 0

for i in range(len(sp) - 1):
    if (sp[i] % 3 == 0 or sp[i + 1] % 3 == 0) and (sp[i] < sr or sp[i + 1] < sr):
        count += 1
        ma = max(sp[i] + sp[i + 1], ma)


print(count, ma)'''

f = open('17_2400.txt')
sp = [int(x) for x in f]
sp.append(0)

count = 0
m = -10000

for i in range(4500):
    if sp[i] + sp[i + 1] >= 100 and (sp[i] < 0 or sp[i + 1] < 0):
        count += 1
        if sp[i] * sp[i + 1] > m:
            m = sp[i] * sp[i + 1]

print(count, m)