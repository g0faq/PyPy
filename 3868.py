s = [int(x) for x in input().split()]
t_room = s[0]
t_cond = s[1]
work = input()
if work == 'freeze':
    if t_room > t_cond:
        print(t_cond)
    else:
        print(t_room)
if work == 'heat':
    if t_room < t_cond:
        print(t_cond)
    else:
        print(t_room)
if work == 'auto':
    print(t_cond)
if work == 'fan':
    print(t_room)