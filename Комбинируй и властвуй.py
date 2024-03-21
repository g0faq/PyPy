s = list(filter(lambda x: x % 9 == 0, range(10, 100)))
s2 = list(map(lambda s: s ** 2, s))
print(sum(s2))