from math import ceil
from random import randrange

with open('output.txt', 'w') as f:

    def dieToss():
        values = [randrange(1, 7) for i in range(20)]
        inRun = False
        for i in range(len(values)-1):
            if inRun:
                if values[i] != values[i-1]:
                    print(')', end=' ')
                    inRun = False
            if values[i] == values[i+1] and not inRun:
                print('(', end=' ')
                inRun = True
            print(values[i], end=' ')
        if inRun:
            print(')', end=' ')
        print()

    def longestSequence():
        store = []
        # Get the first random number
        roll = randrange(1, 7)
        # Set the result to the first roll
        result = str(roll)
        for i in range(19):
            # Get a new roll
            roll = randrange(1, 7)
            # If it is the last roll
            if i == 18:
                # Check if the roll is the same as the previous roll
                if str(roll) in result:
                    # Append the whole string to the store list
                    store.append(result + str(roll))
                else:
                    # If the value is not the same, append the current result
                    store.append(result)
                    # Append the new roll
                    store.append(str(roll))
            else:
                # If the same then continue adding to result
                if str(roll) in result:
                    result += str(roll)
                # If the roll is not the same as the previous roll
                # Append the previous roll, and set the prev roll to the new roll
                else:
                    store.append(result)
                    result = str(roll)
        # Get the length of each string inside the store list
        stringLens = list(map(len, store))
        # Empty string to store values
        finalResult = ''
        # Bool for whether the longest sequence was found
        found = False
        for i in store:
            # If the length of the string is 1, then print the number
            if len(i) == 1:
                finalResult += f'{i} '
            else:
                # Get the index of the biggest string from the list and check whether the current string == longest string
                if i == store[stringLens.index(max(stringLens))] and not found:
                    # Print the brackets accordingly until the string has been iterated through completely
                    for j in range(len(i)):
                        if j == 0:
                            finalResult += f'({i[j]} '
                        elif j == len(i)-1:
                            finalResult += f'{i[j]}) '
                        else:
                            finalResult += f'{i[j]} '
                        # Set found to True
                        found = True
                # If the length of the string > 1, then just concatenate the numbers in the string separately
                else:
                    for j in i:
                        finalResult += j + ' '
        # Print the final result
        print(finalResult)

    def longestFalse(ls):
        # Empty list
        ls = list(map(int, ls))

        store = []
        # Set result to the first bool value
        result = str(ls[0])
        for i in range(1, len(ls)):
            # If the value is False and result has False in it, then add another False to result
            # If the value is not False, then just append it
            if str(ls[i]) == '0' and '0' in result:
                result += str(ls[i])
            else:
                store.append(result)
                result = str(ls[i])
        store.append(result)
        # Map the lengths of the strings from store
        lengths = list(map(len, store))
        # Add up all the lengths before the max section which is equal to first index
        # Last index is the same as adding the length of the string of the first index + the first
        # index and - 1 since we start from 0
        fIndex = sum(lengths[:lengths.index(max(lengths))])
        lIndex = fIndex + len(store[lengths.index(max(lengths))]) - 1
        return (fIndex, lIndex) if fIndex != lIndex else (ls.index(0), ls.index(0))

    def occupy(num):
        # Create a list of all false values and print that list
        ls = [False]*num
        print('_ '*num)
        for i in range(num):
            # Get the start and end index of the largest function from the previous function
            longFasle = longestFalse(ls)
            # Average the average the 2 indexes and get the ceil value from it
            getCenter = ceil((longFasle[0] + longFasle[1]) / 2)
            # Change that index to 1
            ls[getCenter] = True
            # Print the list
            print(''.join(['X ' if i else '_ 'for i in ls]))

    def Pal(ls):
        L = ls[0::]
        L.reverse()
        return ls == L

    if __name__ == "__main__":
        dieToss()
        longestSequence()
        print(longestFalse([False, False, True, False,
                            True, True, True, False, False, False]))
        occupy(10)
        print(Pal([5, 2, 9, 9, 2, 5]))
