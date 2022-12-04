#!/usr/bin/python3
import unittest
from matrices import *


# --------------------------------------------------------------q3.py
# Two-dimensional arrays, simple algorithms
# --------------------------------------------------------------

# --------------------------------------------------------------
# Find the most frequent value in the matrxi
# --------------------------------------------------------------
def mostfrequent(matrix):
    '''
    Returns the value that is most frequent in the matrix
    but in the case of a tie, return the lowest most frequent value
    '''
    dct = {}
    for i in matrix:
        # Get the sorted part of the secondary list
        i.sort()
        for j in i:
            # If the element is not inside the dictionary, add it to the dictionary
            if j not in dct:
                dct[j] = 0
            # Increment the value for the key
            dct[j] += 1
    # Get the list of keys in the dictionary and then sort the list
    dct_keys = list(dct.keys())
    dct_keys.sort()
    # Get all the values based on the sorted keys list
    dct_values = [dct[i] for i in dct_keys]
    # Return the key lowest key with the highest frequency
    return dct_keys[dct_values.index(max(dct_values))]


# ----------------------------------------------------------
# Show the matrices that we imported 
# matrix1, matrix2 and using printmx()
# --------------------------------------------------------------
printmx(matrix1)
printmx(matrix2)
printmx(matrix3)
printmx(matrix4)
printmx(matrix5)
printmx(matrix6)


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(mostfrequent(matrix1), 16)

    def test2(self):
        self.assertEqual(mostfrequent(matrix2), 50)

    def test3(self):
        self.assertEqual(mostfrequent(matrix3), 75)

    def test4(self):
        self.assertEqual(mostfrequent(matrix4), -129)

    def test5(self):
        self.assertEqual(mostfrequent(matrix5), 95)

    def test6(self):
        self.assertEqual(mostfrequent(matrix6), 16)


if __name__ == '__main__':
    unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
