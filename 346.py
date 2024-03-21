a = int(input())
s = []
for i in range(a):
    s.append(int(input()))
count_minus = 0
count_plus = 0
count_zero = 0
for elem in s:
    if elem == 0:
        count_zero += 1
    elif elem > 0:
        count_plus += 1
    elif elem < 0:
        count_minus += 1
print(count_zero, count_plus, count_minus)