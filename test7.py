list_of_ips = [0, 128, 192, 224, 240, 248, 252, 254, 255]
for elem in list_of_ips:
    if 155 & elem == 151 & elem:
        print(elem)
        

print(bin(240)[2:].count('1') + 24)