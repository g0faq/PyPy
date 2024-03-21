s = {}


def add_friends(name_of_person, list_of_friends):
    global s
    if name_of_person in s:
        s[name_of_person] += list_of_friends
    else:
        s[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    global s
    if name_of_person2 in s[name_of_person1]:
        return True
    return False


def print_friends(name_of_person):
    global s
    s[name_of_person].sort()
    print(' '.join(s[name_of_person]))