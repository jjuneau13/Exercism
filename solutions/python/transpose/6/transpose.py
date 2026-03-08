from itertools import zip_longest

def transpose(text):
    spl = text.split('\n')
    iterator = zip_longest(*spl, fillvalue = '_')
    return '\n'.join(''.join(i).rstrip('_').replace('_', ' ') for i in iterator)
        