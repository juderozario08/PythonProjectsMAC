from math import sqrt
from random import randrange


def q1(ls):
    # Iterate through the list of strings backwards and print it
    for i in range(len(ls)-1, -1, -1):
        print(f"String {i+1}/5: {ls[i]}")


def Max(ls):
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
    return (ls[list(map(len, ls)).index(max(list(map(len, ls))))])


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


def functionPerimeterPoly(ls):
    # Using list comprehension, use the perimeter formula and use the coordinates accordinly. x2 - x1 and y2 - y1
    return sum([sqrt((ls[(i+1) % len(ls)][0] - ls[i][0]) ** 2 + (ls[(i+1) % len(ls)][1] - ls[i][1]) ** 2) for i in range(len(ls))])


def permutation(ls):
    return [ls.pop(randrange(0, len(ls))) for i in range(len(ls))]


if __name__ == "__main__":
    # q1([input(f"Enter string {i+1}/5: ") for i in range(5)])
    # Max([100, 'blue', 3.5, 'sugar on the rocks', 7.0])
    # Max([7, 2, 9, 1])
    print(longest(['blue', 'red', 'the white house', 'green']))
    # q4()
    # q5()
    # print(functionPerimeterPoly([(3, 4), (6, 9), (10, -2), (6, -2)]))
    # print(permutation(list(range(0, 30))))


def bowTie(h):
    print(
        ''.join(['*'*(2*i + 1) + ' '*2*(h - (2*i + 1)) + '*'*(2*i + 1)+'\n' for i in range(h//2 + 1)]) + ''.join(
            ['*'*(2*i + 1) + ' '*2*(h - (2*i + 1)) + '*'*(2*i + 1)+'\n' for i in range(h//2 - 1, -1, -1)]))


# bowTie(int(input()))
counter = 0
ls = []
dct = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
for i in range(int(input()), int(input())+1):
    flip = ''
    for j in range(len(str(i))):
        if str(i)[j] not in dct:
            break
        else:
            flip += dct[str(i)[j]]
    if flip[::-1] == str(i):
        counter += 1
    flip = ''
print(counter)
