k, n = [int(x) for x in input().split()]
if k == 1 or k == 2:
    print(0)
else:
    count_k = 0
    for i in range(k):
        for j in range(k):
            count = 0
            if (i - 2) >= 0:
                if (j + 1) < k:
                    count += 1
                if (j - 1) >= 0:
                    count += 1
            if (i + 2) < k:
                if (j + 1) < k:
                    count += 1
                if (j - 1) >= 0:
                    count += 1
            if (i - 1) >= 0:
                if (j + 2) < k:
                    count += 1
                if (j - 2) >= 0:
                    count += 1
            if (i + 1) < k:
                if (j + 2) < k:
                    count += 1
                if (j - 2) >= 0:
                    count += 1
            if count == n:
                count_k += 1
    print(count_k)