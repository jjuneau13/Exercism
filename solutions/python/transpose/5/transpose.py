from itertools import zip_longest
def transpose(text):
    spl = text.split('\n')
    iterator = zip_longest(*spl, fillvalue = '_')
    result = []
    for zipped in iterator:
        result.append(''.join(zipped).rstrip('_').replace('_', ' '))
    return '\n'.join(result)
        