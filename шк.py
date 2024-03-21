a = int(input())
s = []
s = [int(x) for x in str(a)]

print(f'Сумма цифп: {sum(s)}')

c, sym, c2, sym2 = 0, 0, 0, 0
for elem in s:
    if elem % 2 == 0:
        c += 1
        sym += elem
    else:
        c2 += 1
        sym2 += elem
print(f'Количество чётных чисел: {c} , сумма чётных чисел: {sym}')
print(f'Количество нечётных чисел: {c2} , сумма нечётных чисел: {sym2}')

print(f'Максимальная цифра в числe: {max(s)} , минимальная цифра в числе: {min(s)}')


print('----------------------------------------')


x = [int(y) for y in str(int(input()))]
count = 0
for i in range(len(x) - 1):
    c = 0
    while x[i + 1] > i:
        c += 1
    if x[i] == len(x) and x[i + 1]:
        c += 1
    if c > count:
        count = c
print(count)