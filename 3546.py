n = int(input())
for i in range(10 ** (n - 1), int('9' * n)):
    if sum([int(x) for x in str(i)]) == n:
        print(i)