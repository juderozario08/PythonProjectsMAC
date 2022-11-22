from math import ceil
from random import randrange


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
occupy(10)

dct = {17: 37, 11: 8}
dct_keys = list(dct.keys())
dct_keys.sort()
print(dct_keys)


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


mostfrequent([[7, 24, 12], [99, 16, 42], [
             42, 48, 40], [32, 16, 5], [99, 16, 42]])
