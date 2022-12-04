import unittest
from random import randrange
from math import ceil
from sys import setrecursionlimit
setrecursionlimit(100000000)


def longestSequence(ls):
    start, end = 0, 0
    biggestRange, biggestRangeLen = (), 0
    for i in range(len(ls)):
        start = i
        end = i
        while True:
            if i + 1 < len(ls) and ls[i] == ls[i+1]:
                end += 1
                i += 1
            else:
                break
        if end-start > biggestRangeLen:
            biggestRange = (start, end)
            biggestRangeLen = end - start

    if biggestRange != ():
        for i in range(20):
            if biggestRange[0] == i:
                print(f'({ls[i]}', end=' ')
            elif biggestRange[1] == i:
                print(f'{ls[i]})', end=' ')
            else:
                print(ls[i], end=' ')
    else:
        for i in ls:
            print(f"{i} ")
    print()


def longestFalse(ls):
    start, end = 0, 0
    biggestRange, biggestRangeLen = (0, 0), 0
    for i in range(len(ls)):
        start = i
        end = i
        while True:
            if i + 1 < len(ls) and not ls[i] and ls[i] == ls[i+1]:
                end += 1
                i += 1
            else:
                break
        if end-start > biggestRangeLen:
            biggestRange = (start, end)
            biggestRangeLen = end - start
    if biggestRange[1]-biggestRange[0] > 0:
        return biggestRange
    else:
        return (ls.index(False), ls.index(False))


def occupy(N):
    ls = [False]*N
    for i in range(N):
        longestFalseVal = longestFalse(ls)
        ls[ceil((longestFalseVal[0]+longestFalseVal[1])/2)] = True
        print(''.join(['X ' if j else '_ ' for j in ls]))


# longestSequence([randrange(1, 7) for i in range(20)])
# print(longestFalse([bool(randrange(0, 2)) for i in range(10)]))
# occupy(10)

dct = {17: 37, 11: 8}
dct_keys = list(dct.keys())
dct_keys.sort()
# print(dct_keys)


def mostfrequent(matrix):
    '''
    Returns the value that is most frequent in the matrix
    but in the case of a tie, return the lowest most frequent value
    '''
    dct = {}
    for i in matrix:
        i.sort()
        for j in i:
            if j not in dct:
                dct[j] = 0
            dct[j] += 1
    dct_keys = list(dct.keys())
    dct_keys.sort()
    dct_values = [dct[i] for i in dct_keys]
    print(dct_keys[dct_values.index(max(dct_values))])


# mostfrequent([[7, 24, 12], [99, 16, 42], [
#              42, 48, 40], [32, 16, 5], [99, 16, 42]])


def count_dominators(ls):
    # If the length is 0 then return 0
    if ls == []:
        return 0
    ls.reverse()
    # Start the max value from a valid index from the list
    max_i = ls[0]
    dominator = 1
    for i in ls:
        # If the current value is greater than the max value seen so far,
        # then set the max to the current value and increment to dominator
        if i > max_i:
            max_i = i
            dominator += 1
    # Return the dominator
    return dominator


print(count_dominators([42, 7, 12, 9, 2, 5]))
# Create a function "sortNums" that given a list of integers, returns a dictionary where the key is the ten's column, and the value is a list of the one's column.
# ex input: [13, 15, 78, 44, 21, 97, 4, 13, 78]
# ex output:  {1: [3, 5, 3], 7: [8, 8], 4: [4], 2: [1], 9: [7], 0: [4]}

# --------------------------------------------------------------
# YOUR ANSWER HERE
# --------------------------------------------------------------


def sortNums(nums):
    # your code here
    dct = {}
    for i in nums:
        key = i // 10
        value = i % 10
        if key in dct:
            dct[key].append(value)
        else:
            dct[key] = [value]
    return dct
# --------------------------------------------------------------
# Test Cases
# --------------------------------------------------------------


class myTests(unittest.TestCase):
    def sameAnswer(self, numDict, numDict2):
        if (len(dict.keys(numDict)) != len(dict.keys(numDict2))):
            return False

        for key in dict.keys(numDict):
            if (len(numDict[key]) != len(numDict2[key])):
                return False
            for i in range(len(numDict[key])):
                if (numDict[key][i] != numDict2[key][i]):
                    return False

        return True

    def test1(self):
        sorted = sortNums([13, 15, 78, 44, 21, 97, 4, 13, 78])
        self.assertTrue(self.sameAnswer(
            sorted, {1: [3, 5, 3], 7: [8, 8], 4: [4], 2: [1], 9: [7], 0: [4]}))

    def test2(self):
        self.assertEqual(sortNums([]), {})

    def test3(self):
        self.assertEqual(sortNums([1]), {0: [1]})

    def test4(self):
        self.assertEqual(sortNums([1, 1, 1, 1]), {0: [1, 1, 1, 1]})


if __name__ == '__main__':
    unittest.main(exit=True)
