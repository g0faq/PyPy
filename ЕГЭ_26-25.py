f = open('26-k5.txt')
n, k, m = map(int, f.readline().split())
sp = [int(elem) for elem in f]
sp.sort()
print(sp[-m], sum(sp[:k]) // k)