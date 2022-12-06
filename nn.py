from file_work import *
from matrix_init import *
from nn_operational import *

import copy


def study(max_itterations, training_matrix_col, training_seq_num, p, e, a):
    error_s = [100000]

    s_training = download_sequences()
    training_matrix_row = len(s_training[0]) - training_matrix_col - 2

    weights_1 = weights_initialization(training_matrix_col + 1, p)
    weights_2 = weights_initialization(p, 1)

    iter = 0
    while error_sum(error_s) > e and iter < max_itterations:
        error_s = []
        training_m = training_initialization(s_training[training_seq_num], training_matrix_row, training_matrix_col)
        for t_elem_num in range(len(training_m)):
            context = [0]
            tmp_seq = copy.deepcopy(training_m[t_elem_num])
            for pred in range(2):
                matrix_X = tmp_seq[-1 * training_matrix_col:]
                matrix_X.append(context)

                matrix_Y = activation_f(matrix_multiplication(matrix_transporation(matrix_X), weights_1))
                matrix_Z = matrix_multiplication(matrix_Y, weights_2)

                buffer = copy.deepcopy(weights_2)
                weights_2 = W2_calculation(weights_2,
                                           s_training[training_seq_num][training_matrix_col + t_elem_num + pred],
                                           matrix_Y,
                                           matrix_Z[0][0],
                                           a)
                weights_1 = W1_calculation(weights_1,
                                           buffer,
                                           s_training[training_seq_num][training_matrix_col + t_elem_num + pred],
                                           matrix_Z[0][0],
                                           matrix_X,
                                           matrix_Y,
                                           a)

                context = matrix_Z[0]
                tmp_seq.append(matrix_Z[0])
                new_error = (matrix_Z[0][0] - s_training[training_seq_num][training_matrix_col + t_elem_num + pred]) \
                            * (matrix_Z[0][0] - s_training[training_seq_num][training_matrix_col + t_elem_num + pred]) \
                            / 2
                error_s.append(new_error)
        iter += 1
        if iter % 10000 == 0:
            print("Curr iteration: " + str(iter) + " Curr error: " + str(error_sum(error_s)))
    upload_weights(training_matrix_col, weights_1, weights_2)
    print("Education finished")


def predict_nums(user_seq, n):
    columns, weights_1, weights_2 = download_weights()

    data_check(user_seq, columns)

    cont_list = [0]
    for i in range(n):
        matrix_X = user_seq[-1 * columns:]
        matrix_X.append(cont_list)

        matrix_Y = activation_f(matrix_multiplication(matrix_transporation(matrix_X), weights_1))
        matrix_Z = matrix_multiplication(matrix_Y, weights_2)

        user_seq.append(matrix_Z[0])
        cont_list = matrix_Z[0]
        print(matrix_Z[0][0])

    print("prediction redy")
    return
