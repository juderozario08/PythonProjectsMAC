from random import randrange


def q2():
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
