count_if = 0
count_elif = 0
count_else = 0

f = open('olimp_08.10.23_H.py')

for i in range(60):
    s = f.readline()
    count_if += s.count('if')
    count_elif += s.count('elif')
    count_else += s.count('else')

print(count_if)
print(count_elif)
print(count_else)