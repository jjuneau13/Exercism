def tick(matrix):
    if len(matrix) < 2:
        return matrix
    #adding 0s to pad the matrix
    for num in range(len(matrix)):
        matrix[num] = [0] + matrix[num] + [0]
    matrix = [[0 for num in range(len(matrix[1]))]] + matrix + [[0 for num in range(len(matrix[1]))]]
    result = []
    for row in range(1, len(matrix)-1):
        result.append([])
        for col in range(1, len(matrix)-1):
            #summing states of all neighbors
            neighbors = sum([matrix[row-1][state] for state in range(col-1, col+2)] +
                      [matrix[row+1][state] for state in range(col-1, col+2)] +
                      [matrix[row][col-1], matrix[row][col+1]])
            if (matrix[row][col] == 1 and neighbors in {2, 3}) or (matrix[row][col] == 0 and neighbors == 3):
                result[row-1].append(1)
            else:
                result[row-1].append(0)
    return result
    