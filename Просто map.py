def simple_map(transformation, values):
    new = []
    for elem in values:
        new.append(transformation(elem))
    return new

