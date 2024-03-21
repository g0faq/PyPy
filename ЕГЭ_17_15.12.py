f = open('17_15.12.txt')
sp = [int(x) for x in f]

count, m = 0, 0
for i in range(1, len(sp)):
    x, y = sp[i - 1], sp[i]
    if ((x ** 0.5) ** 2 == x and x > 0) or ((y ** 0.5) ** 2 == y and y > 0):
        count += 1
        m = max(m, x + y)

print(count, m)