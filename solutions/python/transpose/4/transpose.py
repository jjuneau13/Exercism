from itertools import zip_longest
def transpose(text):
    spl = text.split('\n')
    iter = zip_longest(*spl, fillvalue = '_')
    result = []
    for zipped in iter:
        result.append(''.join(zipped).rstrip('_').replace('_', ' '))
    return '\n'.join(result)
        