def chekio(matrix):
    for i in matrix:
        for j in matrix[i]:
            if matrix[i][j] == matrix[i][j+1]:
                check_hor(matrix[i][j])
            elif matrix[i][j] == matrix[i+1][j]:
                check_vert(matrix[i][j])
            elif matrix[i][j] == matrix[i+1][j+1]:
                check_diag_r(matrix[i][j])
            elif matrix[i][j] == matrix[i+1][j-1]:
                check_diag_l(matrix[i][j])
