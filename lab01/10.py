def more_ones(matrix):
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] == 1:
                return i + 1
    return 0


assert (more_ones([
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1]
]) == 2)
