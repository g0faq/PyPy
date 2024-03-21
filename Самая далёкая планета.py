def find_farthest_orbit(list_of_orbits):
    s = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    m = 0
    r = (0, 0)
    for elem in s:
        if elem[0] * elem[1] * 3.14 > m:
            m = elem[0] * elem[1] * 3.14
            r = elem
    return r
