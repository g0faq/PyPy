a, b = int(input()), int(input())
s = []
for i in range(a - 1, b + 1):
    if i % 2 == 0:
        s.append(str(i))
print(' '.join(s))