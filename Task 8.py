def add_matrices(matrix1, matrix2):
    result = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print("Resultant matrix:", add_matrices(matrix1, matrix2))