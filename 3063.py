x = int(input())
p = int(input())
y = int(input())
count = 0
while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    count += 1
print(count)