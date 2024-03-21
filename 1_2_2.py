from itertools import product

count = 0
for k in range(2, 11):
    nums = list(product('12345678', repeat=k))
    for elem in nums:
        if elem[-1] == elem[-2]:
            s = sum(map(int, elem))
            if s <= 10:
                count += 1
                print(count )
print(count)
