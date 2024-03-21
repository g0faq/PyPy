hours = input().split()
for elem in hours:
    if int(elem) < 10:
        elem = '0' + elem
minutes = input().split()
for elem in minutes:
    if int(elem) < 10:
        elem = '0' + elem
lucky_list = []
for i in range(61):
    if i < 10:
        i = '0' + str(i)
    for j in range(25):
        if j < 10:
            j = '0' + str(j)
        if str(i) in hours and str(j) in minutes:
            if str(i)[0] + str(i)[1] != str(j)[0] + str(j)[1]:
                lucky_list.append(f'{i}:{j}')
for elem in lucky_list:
    print(elem)