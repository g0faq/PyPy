f = open('26_9379.txt')
n = f.readline()
sp = [int(x) for x in f]

# список ссущих людей по минутам
# time[3] = 6 -> В третью минуту ссало 6 человек
time = [0] * 1443
for elem in sp:
    for i in range(elem, elem + 6):
        time[i] += 1
min_pis = max(time) # самая popular минута (кстати, это 8 вечера)

# ищем минуты, в которые ссало в два раза меньше людей, чем писсуаров
count = 0
for elem in sp:
    f = True
    for element in time[elem:elem + 6]:
        if element > (min_pis + 1) // 2:
            f = False
    if f:
        count += 1

print(min_pis, count)

