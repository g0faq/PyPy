s = [int(x) for x in input().split()]
x = int(input())
c = 1
for elem in s:
    if elem >= x:
        c += 1
print(c)