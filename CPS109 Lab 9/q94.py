#!/usr/bin/python3
import unittest
from matrices import *
# --------------------------------------------------------------q4.py
# Two-dimensional arrays, simple algorithms
# --------------------------------------------------------------

# --------------------------------------------------------------
# is there a repeated row?
# --------------------------------------------------------------
def repeatedrow(matrix) :
    '''
    Returns True if an only if at least one row is the same as another row
    False otherwise
    '''
    # Go thorugh the matrix
    for i in range(len(matrix)):
      # Go through every list after the current list
      for j in range(i+1,len(matrix)):
        # If they are the same, then return True
        if matrix[i] == matrix[j]:
          return True
    # If all checks fail then return False
    return False
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
  self.assertEqual(repeatedrow(matrix1), True)
 def test2(self):
  self.assertEqual(repeatedrow(matrix2), False)
 def test3(self):
  self.assertEqual(repeatedrow(matrix3), False)
 def test4(self):
  self.assertEqual(repeatedrow(matrix4), False)
 def test5(self):
  self.assertEqual(repeatedrow(matrix5), False)
 def test6(self):
  self.assertEqual(repeatedrow(matrix7), True)

if __name__ == '__main__':
 unittest.main(exit=True)


# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
