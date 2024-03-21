s = [int(x) for x in input().split()]
d = s[0]
k = s[1]
new_number = int(str(d)[-1]) ** 5 * 20
for i in range(k - 1):
    new_number += (int(str(new_number)[-1]) ** 5 * 20) + int(str(new_number)[0:-1])
print(new_number)