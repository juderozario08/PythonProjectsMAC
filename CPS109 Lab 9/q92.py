#!/usr/bin/python3
import unittest
from matrices import *


# --------------------------------------------------------------q2.py
# Two-dimensional arrays, simple algorithms
# --------------------------------------------------------------

# --------------------------------------------------------------
# Find the number of values in the matrix that ...
# --------------------------------------------------------------
def count23(matrix):
    '''
    Returns the number of values in the matrix that
    are divisible by both 2 and 3
    '''
    # Go through every element inside the 2d list and then keep only the numbers that are divisible by both 2 and 3
    # Map length to the list to find the length of each element inside the list
    # Then sum up all the lengths to get the number of total elements inside the list
    return sum(map(len, [[j for j in i if j % 2 == 0 and j % 3 == 0] for i in matrix]))


# ----------------------------------------------------------
# Show the matrices that we imported 
# matrix1, matrix2 and using printmx()
# --------------------------------------------------------------
printmx(matrix1)
printmx(matrix2)
printmx(matrix3)
printmx(matrix4)
printmx(matrix5)


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(count23(matrix1), 6)

    def test2(self):
        self.assertEqual(count23(matrix2), 5)

    def test3(self):
        self.assertEqual(count23(matrix3), 20)

    def test4(self):
        self.assertEqual(count23(matrix4), 16)

    def test5(self):
        self.assertEqual(count23(matrix5), 0)


if __name__ == '__main__':
    unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
