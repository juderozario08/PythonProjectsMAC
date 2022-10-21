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


# print(oddBananzaComp([1, 3, 5]))
# print(oddBananzaComp([31, 243, 1255]))
# print(oddBananzaComp([1, 3, 5, 7, 9]))
# print(oddBananzaComp([1, 9, 25, 49, 81, 905]))

def thursday8am(ls):
    if len(ls) == 0:
        return False
    if len(ls) == 1:
        return not ls[0]
    return thursday8am(ls[0:ceil(len(ls)/2)]) and thursday8am(ls[ceil(len(ls)/2):len(ls)]) if (len(ls) % 2 != 0) \
        else thursday8am(ls[0:ceil(len(ls)/2)]) or thursday8am(ls[ceil(len(ls)/2):len(ls)])


print(thursday8am([True, False]))
print(thursday8am([True, False, False]))
print(thursday8am([False, False, True, False, True, True, False, True, True]))
