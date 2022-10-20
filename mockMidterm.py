def sumIndices(string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return sum([alpha.find(i) for i in string if i in alpha])


# print(sumIndices('I went to town!'))

x = 100
eps = 0.000000001


def bisectionSearch(low, high, counter):
    counter += 1
    y = (low+high)/2
    if abs(y**4 - x) <= eps:
        return counter
    if y**4 > x:
        return bisectionSearch(low, y, counter)
    elif y**4 < x:
        return bisectionSearch(y, high, counter)


# print(bisectionSearch(0, x, 0))


def search(guess):
    if abs(guess**2 - 77) > 1:
        return 1+search((guess + (77/guess))/2)
    return 1


print(search(2))


def sumN(number):
    return sum([i for i in range(1, number+1) if number % i == 0])


# print(sumN(4312943))

def sumBinary(L):
    return sum([int(str(i), 2) for i in L])


# print(sumBinary([10100, 101000, 100000, 1011111, 1000, 1010111, 1010010, 11001, 101100,
    #   10111, 11011, 1011010, 11101, 10, 110011, 1001111, 110010, 101100, 100001, 111001]))
