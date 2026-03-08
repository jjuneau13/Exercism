from itertools import zip_longest

def transpose(text):
    spl = text.split('\n')
    iterator = zip_longest(*spl, fillvalue = '_')
    return '\n'.join(''.join(col).rstrip('_').replace('_', ' ') for col in iterator)
        