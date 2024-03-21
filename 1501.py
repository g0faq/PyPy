x = int(input())
v = 'NO'
if x % 4 == 0 and x % 100 != 0:
    v = 'YES'
if x % 400 == 0:
    v = "YES"
print(v)