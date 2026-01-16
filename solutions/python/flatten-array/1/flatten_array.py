def flatten(iterable):
    flat = []
    for i in iterable:
        if isinstance(i, list):
            flat.extend(flatten(i))
        elif i != None:
            flat.append(i)
    return flat