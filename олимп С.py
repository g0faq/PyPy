n, m = int(input()), int(input())
count = 0
while n != 0 and m != 0:
    count += 1
    if count % 2 == 0:
        n += count
        m -= count
    else:
        n -= count
        m += count
print(count)
