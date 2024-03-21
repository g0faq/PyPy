n = int(input())
s = ''
for i in range(n - 1):
    s += input()
for i in range(1, n + 1):
    if str(i) not in s:
        print(i)