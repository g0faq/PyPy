p = [int(x) for x in input().split()]
n, m, k = p[0], p[1], p[2]
if k > n:
    print('NO')
count = 0
while m > 0:
    m -= n
    if m >= 1:
        m += k
        count += 1
    else:
        count += 1
        break
print(count)