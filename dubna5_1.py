count = 0
sp = [0, 1, 2, 3, 4]
for i in range(100, 445):
    f = True
    if int(str(i)[0]) not in sp:
        f = False
    if int(str(i)[1]) not in sp:
        f = False
    if int(str(i)[2]) not in sp:
        f = False

    if f:
        if (int(str(i)[1]) < int(str(i)[0])) and (int(str(i)[2]) < int(str(i)[1])):
            count += 1
            print(i)

print(count)