import unittest
# Note that today's Quiz will be a bit different than usual

# Firstly, you will be completing this individually (no communication)
# Secondly, this will be closed-book (other than the official Python documentation)
# Thirdly, please only make changes where the comments indicate, on this file itself
# Finally, to get full marks, you must complete all 7/7 tasks

# Your first task is to create a function called find_highest_value that finds the highest value of some input list of floats L and returns its index
# TODO: Complete find_highest_value


def find_highest_value(L):
    return L.index(max(L))

# Your second task will be to create a function called remove_all_ees that takes in a string s and returns the string with all instances of the substring
# 'ee' removed (don't remove single 'e's)
# TODO: complete remove_all_ees


def remove_all_ees(S):
    return S.replace('ee', '')

# Your third task will be to create a function called find_smallest_div that takes in two nonempty lists of integers and returns the indices of the two
# (one from each list) that, when divided, give the smallest quotient. Return as a tuple.
# TODO: complete find_smallest_div


def find_smallest_div(L1, L2):
    L1max = [L1[0], 0]
    L1min = [L1[0], 0]
    L2max = [L2[0], 0]
    L2min = [L2[0], 0]
    for i in range(max(len(L1), len(L2))):
        if i < len(L1):
            if L1[i] < L1min[0]:
                L1min = [L1[i], i]
            if L1[i] > L1max[0]:
                L1max = [L1[i], i]
        if i < len(L2):
            if L2[i] < L2min[0]:
                L2min = [L2[i], i]
            if L2[i] > L2max[0]:
                L2max = [L2[i], i]
    result1 = L1max[0]/L2max[0]
    result2 = L1min[0]/L2max[0]
    result3 = L2max[0]/L1max[0]
    result4 = L2min[0]/L1max[0]
    minRes = min(result1, result2, result3, result4)
    if minRes == result1 or minRes == result3:
        return (L1max[1], L2max[1])
    if minRes == result2:
        return (L1min[1], L2max[1])
    return (L1max[1], L2min[1])

# Your fourth task will be to create a recursive function rec_add that takes in a list of integers L and if there is one element returns it plus 2,
# else it returns the value of the last integer in the list plus rec_add of the list minus that element
# TODO: complete rec_add


def rec_max(ls, maxValue):
    if len(ls) == 1:
        return maxValue
    elif len(ls) == 2:
        return ls[0] if ls[0] > ls[1] else ls[1]
    temp = ls.pop()
    if maxValue < temp:
        maxValue = temp
    return rec_max(ls, maxValue)


print(rec_max([1, 2, 3, 5, 6, 77, 100, 121], 1))


def rec_add(L):
    return L[0] + 2 if len(L) == 1 else L.pop()+rec_add(L)

# Your fifth task will be to complete all unittests here.


class QuizTestCases(unittest.TestCase):
    def test_1_find_highest_value_normal(self):  # An example for you...
        self.assertEqual(find_highest_value([4, 5, 3, 3, 0, -3]), 1)

    # Create a test case for the remove_all_ees function
    def test_2_remove_all_ees(self):
        self.assertEqual(remove_all_ees('creeek'), 'crek')

    # Create TWO test cases for the find_smallest_div function
    def test_3_find_smallest_div(self):
        self.assertEqual(find_smallest_div([1, 4], [2, 4]), (0, 1))

    # ... hint: consider lists with negative values (for the find_smallest_div function)
    def test_4_find_smallest_div_negative(self):
        self.assertEqual(find_smallest_div(
            [10, 2, 4, 5], [-1, -2, -3, -0.25]), (0, 3))

    def test_5_rec_add(self):  # Create a test case for the rec_add function
        self.assertEqual(rec_add([4, 6, 7]), 19)


if __name__ == "__main__":
    print("Running quiz")

    # # Your sixth last task is to create some string, call the remove_all_ees function on that string such that it permanently changes the string,
    # # then print that edited string
    # # TODO: do the above
    # string = 'creek reek flake'
    # string = remove_all_ees(string)
    # print(string)

    # # Your final task will be to call the find_highest_value function on a list, such that it returns the value 4. You pick the list so that this is the case.
    # # TODO: do the above
    # L = [1, 2, 4, -2, 5, -5]
    # print(find_highest_value(L))

    unittest.main(exit=True)
