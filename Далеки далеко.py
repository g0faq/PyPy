import sys

sentenses = map(str.strip, sys.stdin)
count = 0
for element in sentenses:
    element = element.lower()
    words = element.split()
    for elem in words:
        if elem == 'далек' or\
                elem == 'далеки' or\
                elem == 'далека' or\
                elem == 'далеков' or\
                elem == 'далеку' or\
                elem == 'далекам' or\
                elem == 'далеком' or\
                elem == 'далеками' or\
                elem == 'далеке' or\
                elem == 'далеках':
            count += 1
            break
print(count)
