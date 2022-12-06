import random


def weights_initialization(rows, columns):
    WEIGHTS = [[random.randint(-1, 1) / 100 for first in range(columns)] for second in range(rows)]
    return WEIGHTS


def training_initialization(seq, rows, columns):
    training_mtx = [[0 for first in range(columns)]
                    for second in range(rows)]
    for row in range(rows):
        for column in range(columns):
            training_mtx[row][column] = [seq[row + column]]
    return training_mtx
