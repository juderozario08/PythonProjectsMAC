#!/usr/bin/python3
import random

random.seed(23)


# ----------------------------------------------------------matrices.py
# This file will be used for importing the print matrix function
# and the example matrices.
# ----------------------------------------------------------
# ----------------------------------------------------------
# Generating a random matrix of integers
# --------------------------------------------------------------
def makematrix(m, n, low=0, high=100):
    matrix = []  # empty matrix
    for i in range(m):
        row = n * [0]
        for j in range(n):
            row[j] = random.randint(low, high)
        matrix.append(row)
    return matrix


# ----------------------------------------------------------
# Printing a matrix of numbers
# --------------------------------------------------------------
def printmx(mx):
    for i in range(len(mx)):
        printrow(mx[i])
    print('-------------------')


def printrow(row):
    for i in range(len(row)):
        print('{:5}'.format(row[i]), end='')
    print()


# ----------------------------------------------------------
# Defining a couple of matrices to try out the printing
# --------------------------------------------------------------
matrix1 = [[7, 24, 12], [99, 16, 42], [42, 48, 40], [32, 16, 5], [99, 16, 42]]
matrix2 = [[7, 24, 7, 1, 2], [50, 16, 50, 3, 4], [42, 48, 42, 5, 6], [32, 16, 32, 7, 8], [50, 1, 50, 9, 10]]
matrix3 = makematrix(7, 15)
matrix4 = makematrix(7, 15, -200, -100)
matrix5 = makematrix(1, 1)
matrix6 = [[17, 24, 12], [17, 16, 42], [17, 48, 40], [101, 16, 5], [99, 16, 42]]
matrix7 = matrix4[0:3]
matrix7.append(matrix4[0])
matrix7.append(matrix4[4])
# ----------------------------------------------------------
# Printing the matrices, but only if this file is run, not imported
# --------------------------------------------------------------
if __name__ == '__main__':
    print('matrix1:\n----------------')
    printmx(matrix1)
    print('matrix2:\n----------------')
    printmx(matrix2)
    print('matrix3:\n----------------')
    printmx(matrix3)
    print('matrix4:\n----------------')
    printmx(matrix4)
    print('matrix5:\n----------------')
    printmx(matrix5)
    print('matrix6:\n----------------')
    printmx(matrix6)
    print('matrix7:\n----------------')
    printmx(matrix7)
# ----------------------------------------------------------
# The End
# --------------------------------------------------------------
