def same_by(characteristic, objects):
    new = list(map(characteristic, objects))
    return all(list(map(lambda x: x == new[0], new)))
