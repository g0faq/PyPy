n = int(input())
sam = 0
for i in range(len(str(n))):
    sam += int(str(n)[i])
for i in range(n + 1):
    if i == sam:
        print(i)