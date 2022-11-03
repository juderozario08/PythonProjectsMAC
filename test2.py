
from math import ceil
results = {1: 1, 2: 1}


def fib(n):
    if n in results:
        return results[n]
    results[n] = fib(n-1)+fib(n-2)
    return results[n]


# print(fib(40))


def perfSquare(number):
    counter = 0
    for i in range(number//2):
        if i ** 2 < number:
            counter += 1
        else:
            break
    return counter


# print(perfSquare(3**4**5))
def lockerStuff():
    lockers = [False]*100
    studentNum = 1
    i = 0
    while studentNum <= 100:
        lockers[i] = True if not lockers[i] else False
        i += studentNum
        if i >= 100:
            studentNum += 1
            i = 0
    print(lockers)
    return sum(lockers)


# print(lockerStuff())
# file = open('output.txt')
# text = (iter(file))
# while file.readline() != '':
#     print(next(text))

# counter = 0
# result = 0
# while counter < 10**9:
#     result += counter
#     counter += 1
# print(result)

def odd_nums(limit):
    num = 1
    while num <= limit:
        yield num
        num += 2


num = int(input())
den = int(input())
if num % den == 0:
    print(num//den)
else:
    # Goofy ass formula
    new_num = num % den
    new_dem = den

    while True:
        remainder = new_num % new_dem
        print(num, den, new_num, new_dem, remainder)
        if remainder == 0:
            break
        else:
            new_num = new_dem
            new_dem = remainder

    print(f"{num//den} {ceil(new_dem/new_num)}/{new_num//new_dem}")
