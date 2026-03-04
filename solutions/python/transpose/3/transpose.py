def transpose(text):
    spl = text.split('\n')
    result = ['' for _ in range(max((len(s) for s in spl), default = 0))]
    for row in range(len(spl)):
        for column in range(len(result)):
            if len(spl[row]) > column:
                if len(result[column]) < row:
                    result[column] += ' ' * (row - len(result[column])) 
                result[column] += spl[row][column]
    return '\n'.join(result)
    