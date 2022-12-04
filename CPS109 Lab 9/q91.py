#!/usr/bin/python3
import unittest
from matrices import *


# --------------------------------------------------------------q1.py
# Two-dimensional arrays, simple algorithms
# --------------------------------------------------------------

# --------------------------------------------------------------
# Find the maximum value in a 2D array
# --------------------------------------------------------------
def maxvalue(matrix):
    '''
    Returns the maximum value in the matrix
    '''
    # Go through every matrix and find every max from the 2d list. Then return the max from the final list
    return max([max(i) for i in matrix])


# ----------------------------------------------------------
# Show the matrices that we imported 
# matrix1, matrix2 and using printmx()
# --------------------------------------------------------------
printmx(matrix1)
printmx(matrix2)
printmx(matrix3)
printmx(matrix4)
printmx(matrix5)
# ----------------------------------------------------------
# Try out the functions on matrix1 and matrix2
# --------------------------------------------------------------
print('The biggest value in matrix1 is {}'.format(maxvalue(matrix1)))
print('The biggest value in matrix2 is {}'.format(maxvalue(matrix2)))
print('The biggest value in matrix3 is {}'.format(maxvalue(matrix3)))
print('The biggest value in matrix4 is {}'.format(maxvalue(matrix4)))
print('The biggest value in matrix5 is {}'.format(maxvalue(matrix5)))


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(maxvalue(matrix1), 99)

    def test2(self):
        self.assertEqual(maxvalue(matrix2), 50)

    def test3(self):
        self.assertEqual(maxvalue(matrix3), 100)

    def test4(self):
        self.assertEqual(maxvalue(matrix4), -100)

    def test5(self):
        self.assertEqual(maxvalue(matrix5), 95)


if __name__ == '__main__':
    unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
