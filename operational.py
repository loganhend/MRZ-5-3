
def matrix_transporation(matrix):
    return [[matrix[first][second] for first in range(len(matrix))]
            for second in range(len(matrix[0]))]


def matrix_multiplication(matrix_A, matrix_B):
    row_number_A = len(matrix_A)
    col_number_A = len(matrix_A[0])
    row_number_B = len(matrix_B)
    col_number_B = len(matrix_B[0])
    if col_number_A != row_number_B:
        print("Cannot multiply the two matrices. Incorrect dimensions")
        return
    else:
        matrix_C = [[0 for col in range(col_number_B)]
                    for row in range(row_number_A)]
        for first_A_index in range(row_number_A):
            for second_B_index in range(col_number_B):
                for second_A_index in range(col_number_A):
                    matrix_C[first_A_index][second_B_index] += matrix_A[first_A_index][second_A_index] \
                                                               * matrix_B[second_A_index][second_B_index]
        return matrix_C


def had_product(matrix_A, matrix_B):
    if matrix_A == matrix_B and matrix_A[0] == matrix_B[0]:
        print("Multiplication impossible")
        return
    else:
        return [[matrix_A[first][second] * matrix_B[first][second] for second in range(len(matrix_A[0]))]
                for first in range(len(matrix_A))]


def df_activation(X):
    for i in range(len(X)):
        for j in range(len(X[0])):
            if X[i][j] > 1:
                X[i][j] = 1
            else:
                X[i][j] = 0.01
    return X


def activation_f(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] >= 0:
                if matrix[row][column] > 1:
                    matrix[row][column] = 1
                else:
                    matrix[row][column] = matrix[row][column]
            if matrix[row][column] < 0:
                matrix[row][column] = matrix[row][column] * 0.01
    return matrix
