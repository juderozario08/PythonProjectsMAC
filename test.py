import unittest
from math import ceil
from random import randrange


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

def recursivePal(s):
    if len(s) < 2:
        return True
    elif len(s) == 2 and s[0] == s[1]:
        return True
    return s[0] == s[len(s)-1] and recursivePal(s[1:len(s)-1])


# print(recursivePal('raceca'))


class QuizTestCases(unittest.TestCase):
    def test_1_noStirng(self):
        self.assertTrue(recursivePal(''))

    def test_1_twoString(self):
        self.assertTrue(recursivePal('aa'))

    def test_1_twoStringF(self):
        self.assertFalse(recursivePal('ab'))

    def test_1_oneStirng(self):
        self.assertTrue(recursivePal('a'))

    def test_1_fullString(self):
        self.assertTrue(recursivePal('racecar'))

    def test_1_fullStringF(self):
        self.assertFalse(recursivePal('raceca'))


if __name__ == "__main__":
    # unittest.main(exit=True)
    pass
    string = 'creekeee'
    print(string.replace('ee', ''))
