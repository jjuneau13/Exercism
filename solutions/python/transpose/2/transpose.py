def transpose(text):
    spl = text.split('\n')
    result = ['' for row in range(max((len(s) for s in spl), default = 0))]
    for row, letter in enumerate(spl):
        for column, group in enumerate(result):
            if len(spl[row]) > column:
                if len(result[column]) < row:
                    result[column] += ' ' * (row - len(result[column])) 
                result[column] += spl[row][column]
    return '\n'.join(result)
    