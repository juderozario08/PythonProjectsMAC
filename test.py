import gzip
from math import ceil


def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)


# print(factorial(5))


def oddBananza(ls):
    # If the list length is 0 then return 0 (exit clause 1)
    if len(ls) == 0:
        return 0
    # If the list length is 1 then return the condition provided by the problem
    if len(ls) == 1:
        return 10-(ls[0] % 10)
    # Else do the recursive call and multiply the condition with it
    return (10-(ls.pop() % 10))*oddBananza(ls)


# print(oddBananza([1, 3, 5]))


def oddBananzaComp(ls):
    # If the list length is 0 then return 0 (exit clause 1)
    if len(ls) == 0:
        return 0
    # If the list length is 1 then return the condition provided by the problem
    if len(ls) == 1:
        return 10-(ls[0] % 10)
    # Else do the recursive call and multiply the condition with it
    secondHalf = [ls.pop() for i in range(len(ls)//2)]
    return oddBananzaComp(ls)*oddBananzaComp(secondHalf)


# x = "sara"
# print("   x    x\nx xx x\nx   x   x".replace("x", x))
# for i in range(5):
#     print(" "*i+x+" "*(9-i*2), x)
# print(" "*6, x)


if __name__ == '__main__':
    print()
