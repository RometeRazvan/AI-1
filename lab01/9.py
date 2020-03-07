def suma_submatrice(mat, first_point, second_point):
    sum = 0
    for i in range(first_point[0], second_point[0]+1):
        for j in range(first_point[1], second_point[1]+1):
            sum += mat[i][j]
    return sum


assert (suma_submatrice([[0, 2, 5, 4, 1],
                         [4, 8, 2, 3, 7],
                         [6, 3, 4, 6, 2],
                         [7, 3, 1, 8, 3],
                         [1, 5, 7, 9, 4]],
                        [1, 1], [3, 3]) == 38)
