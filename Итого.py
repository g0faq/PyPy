with open('prices.txt', 'r', encoding='utf8') as file:
    read_file = file.readlines()
s = 0
for elem in read_file:
    a = elem.split()
    s += int(a[1]) * float(a[2])
print('{:.2f}'.format(s))
