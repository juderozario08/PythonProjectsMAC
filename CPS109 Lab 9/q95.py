#!/usr/bin/python3
import unittest
from matrices import *
from q94 import repeatedrow
from itertools import zip_longest

# --------------------------------------------------------------q4.py
# Two-dimensional arrays, simple algorithms
# --------------------------------------------------------------
def transpose(matrix) :
    '''
    Returns a matrix which is the transpose of the argument matrix.
    Assumes that the matrix is retangular
    '''
    # Go through every secondary list and get the element in the i'th position inside the list
    # Continue until we are done iterating through the column number of times
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# --------------------------------------------------------------
# is there a repeated column?
# --------------------------------------------------------------
def repeatedcolumn(matrix) :
    '''
    Returns True if an only if at least one column is the same as another column
    False otherwise
    Use the transpose() method as a helper method, along with the 
    repeatedrow() method from q4.py
    '''
    # Get the transposed list and then check whether there is a repeated row in the matrix
    return repeatedrow(transpose(matrix))
# ----------------------------------------------------------
# Show the matrices that we imported 
# matrix1, matrix2 and using printmx()
# --------------------------------------------------------------
for matrix in [matrix1, matrix2, matrix3, matrix4, matrix5] :
    printmx(matrix)
    print('transpose:')
    printmx(transpose(matrix))

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(repeatedcolumn(matrix1), False)
 def test2(self):
  self.assertEqual(repeatedcolumn(matrix2), True)
 def test3(self):
  self.assertEqual(repeatedcolumn(matrix3), False)
 def test4(self):
  self.assertEqual(repeatedcolumn(matrix4), False)
 def test5(self):
  self.assertEqual(repeatedcolumn(matrix5), False)
if __name__ == '__main__':
 unittest.main(exit=True)


# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
