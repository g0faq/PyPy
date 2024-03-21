s = open('24_15.12.txt').read()
res = 0
count = 1
for i in range(1, len(s)):
    if int(s[i]) > int(s[i - 1]):
        count += 1
    else:
        res = max(res, count)
        count = 1

print(res)