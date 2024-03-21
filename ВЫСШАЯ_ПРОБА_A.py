import time

n, a, b = int(input()), int(input()), int(input())

def nod(a, b):
    while b != 0:
        a, b = b, a % b
        return a

n0d = nod(a, b)
res = [1, n0d]
for i in range(1, res[1] + 1):
    if res[1] % i == 0:
        res[0] = max(res[0], i)

print(res[0])
print(res[1])