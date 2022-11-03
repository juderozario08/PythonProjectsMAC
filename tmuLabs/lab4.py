# Write a program that has a loop to read in five strings and put them into a list. Write a
# second loop to print the strings in the reverse order. This is an exercise in indexing, so do
# not use the reverse() method of list. Print the index in the following format. The actual
# strings you read in are arbitrary. Example format when running q1.py:
# Enter string 1/5: the blue moon
# Enter string 2/5: the red guitar
# Enter string 3/5: go home
# Enter string 4/5: spill the beans
# Enter string 5/5: winter in Oklahoma
# String 5/5: winter in Oklahoma
# String 4/5: spill the beans
# String 3/5: go home
# String 2/5: the red guitar
# String 1/5: the blue moon

from math import sqrt
from random import randrange


def q1(ls):
    for i in range(len(ls)-1, -1, -1):
        print(f"String {i+1}/5: {ls[i]}")

# Write a function max(L) which examines the argument list L, and returns the largest object
# of type float. If there is no float object in the list, then the function returns None. For
# example:
# max([100, ‘blue’, 3.5, ‘sugar on the rocks’, 7.0]) would return 7.0, and
# max([7, 2, 9, 1]) would return None.
# Note that type(element) == float is a way to check if element is a float.
# 3. Write a function longest(L) which examines the argument list L and returns the longest
# string. You can assume all of the elements of the list L are strings, and that the list is not
# empty. Use the approach where there is a variable largestyet which is initialized to the first
# element of L. Then go through the rest of the elements and update largestyet whenever
# you encounter a longer string. For example”
# longest(['blue', 'red', 'the white house', 'green']) would return 'the white house'.


def q2(ls):
    floatLs = []
    for i in ls:
        if type(i) == float:
            floatLs.append(i)
    print('None' if len(floatLs) == 0 else max(floatLs))


def q3(ls):
    lengths = list(map(len, ls))
    print(ls[lengths.index(max(lengths))])


def q4():
    listNum, tupleNum = [], ()
    listOdd, tupleOdd = [], ()
    listSquares, tupleSquares = [], ()
    listRandom, tupleRandom = [], ()
    listZeroes, tupleZeroes = [], ()
    for i in range(101):
        listNum.append(i)
        tupleNum += (i,)
    for i in range(1, 102, 2):
        listOdd.append(i)
        tupleOdd += (i,)
    for i in range(50):
        listSquares.append(i**2)
        tupleSquares += (i**2,)
    for i in range(60):
        randomNum = randrange(0, 50)
        listRandom.append(randomNum)
        tupleRandom += (randomNum,)
    for i in range(50):
        listZeroes.append(0)
        tupleZeroes += (0,)
    print(listNum, tupleNum)
    print(listOdd, tupleOdd)
    print(listSquares, tupleSquares)
    print(listRandom, tupleRandom)
    print(listZeroes, tupleZeroes)


def q5():
    print([i for i in range(101)])
    print([i for i in range(1, 102, 2)])
    print([i**2 for i in range(50)])
    print([randrange(0, 50) for i in range(60)])
    print([0 for i in range(50)])


def q6():
    print(qrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


if __name__ == "__main__":
    # q1([input(f"Enter string {i+1}/5: ") for i in range(5)])
    # q2([100, 'blue', 3.5, 'sugar on the rocks', 7.0])
    # q2([7, 2, 9, 1])
    # q3(['blue', 'red', 'the white house', 'green'])
    # q4()
    # q5()
    q6()
