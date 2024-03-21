s1 = int(input())
h = s1 // 3600 % 24
m = (s1 // 60 % 60)
s = s1 % 60
print(str(h) + ':' + str(m // 10) + str(m % 10) + ':' + str(s // 10) + str(s % 10))