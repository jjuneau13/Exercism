def is_paired(input_string):
    open = '[{('
    closed = ']})'
    l1 = []
    for char in input_string:
        if char in open:
            l1.append(char)
        if char in closed:
            if len(l1) == 0:
                return False
            last = l1.pop()
            if open.index(last) != closed.index(char):
                return False
    return len(l1) == 0
