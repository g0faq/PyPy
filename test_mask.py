mask = '1?7602*0'
number = '1076027890'

digits = list(mask)
nums = list(number)

print(digits)
print(nums)

f = True
x = 0

if mask.count('*') == 1:
    for i in range(5, len(digits)):
        if digits[i] == '*':
            x += len(nums) - len(digits)
        elif digits[i] != nums[i + x] and digits[i] != '?':
            f = False
            break

print(f)
