sp = [int(x) for x in input().split()]
m = int(input())
a = max(sp)
if a >= m:
    if a % 2 != 0:
        print((a + 1) // m)
    else:
        print(a // m)
else:
    print(1)