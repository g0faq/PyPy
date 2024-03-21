count, res = 0, 0
for i in range(30001, 70001):
    c = 2
    print(i)
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            c += 1
            if c > 17:
                break
    if c == 17:
        if count == 0:
            res = i
        count += 1

print(count, res)