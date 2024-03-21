f = open('26-k4.txt')
n, k = map(int, f.readline().split())
sp = [int(elem) for elem in f]
sp.sort(reverse=True)
print(sum(sp[k:2 * k]) // k, sum(sp[:k]) // k)