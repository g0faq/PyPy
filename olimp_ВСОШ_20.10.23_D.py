import time

q = time.perf_counter()

n, x, y = int(input()), int(input()), int(input())
count_res = 0
for i in range(1, n + 1):
    dop_count = [len(str(i)), 0]
    for elem in str(i):
        dop_count[1] += 1 if elem == str(x) or elem == str(y) else 0
    count_res += 1 if dop_count[0] == dop_count[1] else 0

print(count_res if count_res > 0 else -1)

print(time.perf_counter() - q)