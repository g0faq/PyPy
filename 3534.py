n, k = int(input()), int(input())
n_ = 1
k_ = 1
n_k = 1
for i in range(1, n + 1):
    n_ *= i
for i in range(1, k + 1):
    k_ *= i
for i in range(1, n - k + 1):
    n_k *= i

print(n_ // (k_ * n_k))