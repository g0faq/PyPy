f = open('26-46.txt')
sp = [int(x) for x in f]
n = sp[0]
del sp[0]

count, res = 0, max(sp) + 1

for i in range(n - 2):
    print(f'i: {i}')
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a, b, c = sp[i], sp[j], sp[k]
            if (a + b + c) % 3 == 0 and (a + b + c) // 3 in sp:
                count += 1
                res = min(res, (a + b + c) // 3)


print(count, res)