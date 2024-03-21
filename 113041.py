a = int(input())
b = int(input())
x = []
for i in range(a, b + 1, 5):
    x.append(i)
for i in range(1, len(x) +  1):
    print(x[-i])