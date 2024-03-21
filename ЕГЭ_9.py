f = open('ЕГЭ_9.txt')
count = 0
for i in range(5000):
    sp = [int(x) for x in f.readline().split()]
    if sp[0] + sp[1] > sp[2] and sp[0] + sp[2] > sp[1] and sp[1] + sp[2] > sp[0]:
        count += 1

print(count)