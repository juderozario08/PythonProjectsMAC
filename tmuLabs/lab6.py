from math import sqrt
from random import randrange


def q1(ls):
    # Iterate through the list of strings backwards and print it
    for i in range(len(ls)-1, -1, -1):
        print(f"String {i+1}/5: {ls[i]}")


def max(ls):
    # Iterate through the list and if there is a float, set the value of float to the largest float value
    floatVal = 0
    for i in ls:
        if type(i) == float:
            if floatVal < i:
                floatVal = i
    # Return none if no float values were seen else return the largest float value
    print('None' if floatVal == 0 else floatVal)


def longest(ls):
    # Iterate through the list and find set result to the largest possible string
    result = ''
    for i in ls:
        if len(result) < len(i):
            result = i
    print(result)


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
    # Same as question 4 but just using list comprehension and only printing lists
    print([i for i in range(101)])
    print([i for i in range(1, 102, 2)])
    print([i**2 for i in range(50)])
    print([randrange(0, 50) for i in range(60)])
    print([0 for i in range(50)])


def functionPerimeterPoly(listOfTuples):
    # Using list comprehension, use the perimeter formula and use the coordinates accordinly. x2 - x1 and y2 - y1
    # Then after getting the sum of that list, do the wrap around to use the formula on the last and first coordinates of the list.
    # Return the final sum
    return sum([sqrt((listOfTuples[i+1][0] - listOfTuples[i][0])
                     ** 2 + (listOfTuples[i+1][1] - listOfTuples[i][1]) ** 2) for i in range(len(listOfTuples)-1)]) + (
        sqrt((listOfTuples[0][0] - listOfTuples[len(listOfTuples)-1][0])**2 + (
            listOfTuples[0][1] - listOfTuples[len(listOfTuples)-1][1])**2))


def permutation(ls):
    # Create the empty list
    permutate = []
    # Create the copy of the users input as a list
    copy = list(ls)
    # While the list in not empty, keep generating a random index and pop that index and add that to the new list
    while len(copy) != 0:
        permutate.append(copy.pop(randrange(0, len(copy))))
    # Return the new list
    return permutate


if __name__ == "__main__":
    # q1([input(f"Enter string {i+1}/5: ") for i in range(5)])
    # max([100, 'blue', 3.5, 'sugar on the rocks', 7.0])
    # max([7, 2, 9, 1])
    # longest(['blue', 'red', 'the white house', 'green'])
    # q4()
    # q5()
    # print(functionPerimeterPoly([(3, 4), (6, 9), (10, -2), (6, -2)]))
    print(permutation(range(0, 30)))
