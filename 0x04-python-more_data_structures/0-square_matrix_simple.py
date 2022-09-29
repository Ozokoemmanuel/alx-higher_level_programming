#!/usr/bin/python3

# Computes the square value of integers in a matrix
# matrix is a 2-d array
# Return value = new_matrix(same size as matrix)
# Each value should be the square of the input
# Initial matrix should not be modified
# No import, no regular loops

def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    return [[i ** 2 for i in column] for column in matrix]
