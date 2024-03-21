LIST = []
for _ in range(int(input())):
    LIST.append(int(input()))
    LIST.sort()

s = 0
while len(LIST) != 1:
    s += max(LIST)
    del LIST[LIST.index(max(LIST))]

print(str(s + 1))