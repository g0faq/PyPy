s = input()
sl = {}
for elem in s.split():
    if elem not in sl:
        sl[elem] += 1

print(sl)