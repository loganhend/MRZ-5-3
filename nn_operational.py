from operational import *


def error_sum(error_list):
    error_res = 0
    for attempt in range(len(error_list)):
        error_res += error_list[attempt]
    return error_res


def error_hidden(weights_2, g):
    return matrix_a(weights_2, g)


def dt(matrix_A, matrix_B):
    return [[matrix_A[first][second] - matrix_B[first][second] for second in range(len(matrix_A[0]))]
            for first in range(len(matrix_A))]


def matrix_a(matrix, a):
    return [[a * matrix[first][second] for second in range(len(matrix[0]))] for first in range(len(matrix))]


def W2_calculation(weights_2, standard, matrix_Y, element_Z, a):
    return dt(weights_2, matrix_a(matrix_a(matrix_transporation(matrix_Y), element_Z - standard), a))


def W1_calculation(weights_1, weights_2, standard, element_Z, matrix_X, Y, a):
    hiddden_r = error_hidden(weights_2, element_Z - standard)
    dvt = matrix_transporation(df_activation(matrix_multiplication(matrix_transporation(matrix_X), weights_1)))
    d_W1 = matrix_a(matrix_multiplication(matrix_X, matrix_transporation(had_product(hiddden_r, dvt))), a)
    return dt(weights_1, d_W1)


def data_check(seq, columns):
    if len(seq) < columns:
        print("Data is not suitable")
        return
