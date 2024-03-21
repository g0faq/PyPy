import sys


sentenses = map(str.strip, sys.stdin)
count = 0
for elem in sentenses:
    elem = elem + '....'
    elem = elem.lower()
    for i in range(len(elem)):
        if elem[i] == 'д' and\
            elem[i + 1] == 'а' and\
            elem[i + 2] == 'л' and\
            elem[i + 3] == 'е' and\
                elem[i + 4] == 'к':
            count += 1
            break
print(count)