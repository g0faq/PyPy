s = [int(a) for a in input().split()]
for elem in s:
    if elem % 2 == 0:
        print(elem, end=' ')