"""
Student Name: Jude Rozario
Student ID: 501166063
Assignment 2
"""
from sys import setrecursionlimit
def is_ascending(items):
    # If the list is empty, return False
    if len(items) == 0:
        return False
    # If the current element is greater than or equal to the next element, then return False
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False
    # Return True if no other conditions have met
    return True


# Done
def riffle(items, out=True):
    # Return the empty list if the list is empty
    if len(items) == 0:
        return []
    # Get the first half of the list
    ls1 = items[:len(items) // 2]
    # Get the second half of the list
    ls2 = items[len(items) // 2:]
    finalList = []
    for i in range(len(ls1)):
        # If 'out' is true, then add first half then second half
        if out:
            finalList.append(ls1[i])
            finalList.append(ls2[i])
        # If 'out' is false, then add second half then first half
        else:
            finalList.append(ls2[i])
            finalList.append(ls1[i])
    # Return the final list
    return finalList


def only_odd_digits(n):
    # If one of the digits in the number is even, return false
    for i in str(n):
        if int(i) % 2 == 0:
            return False
    # If the previous conditions have not met, return True
    return True


def domino_cycle(tiles):
    # If there are no tiles, then return True
    if len(tiles) == 0:
        return True
    # If it is of length 1, check if it is a loop
    if len(tiles) == 1:
        return tiles[0][0] == tiles[0][1]
    # Go through each tile and check if the last placement and the next placement is the same
    # If they are not, then return False. Else continue to search
    for i in range(len(tiles) - 1):
        if tiles[i][1] != tiles[i + 1][0]:
            return False
    # If all other checks have passed, check if the start and end position is the same
    return tiles[0][0] == tiles[-1][1]


def is_cyclops(n):
    # Convert the number to a string
    num = str(n)
    # If the length of the string is even, return False
    if len(num) % 2 == 0:
        return False
    # If the middle position is not 0, then return False
    if num[len(num) // 2] != '0':
        return False
    for i in range(len(num)):
        # If it is not the middle position and the other numbers are not 0 then continue\
        if i != len(num) // 2 and num[i] == '0':
            return False
    # If all checks passed then return true
    return True


dct_colors = {'rb': 'y', 'br': 'y', 'by': 'r', 'yb': 'r', 'ry': 'b', 'yr': 'b','bb':'b','rr':'r','yy':'y', 'r':'r', 'b':'b', 'y':'y'}
# def colour_trio(colours):
#     result = ''
#     while True:
#         # Return the value from the key using the hashmap if the number of colours are 2 or lower
#         if len(colours) <= 2:
#             return dct_colors[colours]
#         for i in range(len(colours) - 1):
#             # Add the values in a temporary result variable that gets values from the keys inside the hashmap
#             result += dct_colors[colours[i] + colours[i + 1]]
#         # Set the colours to result
#         colours = result
#         result = ''

def colour_trio(colours):
    if len(colours) == 1:
        return colours
    result = ''
    for i in range(len(colours)-1):
        if colours[i] == 'r':
            if colours[i+1] == 'b':
                result += 'y'
            elif colours[i+1] == 'r':
                result += 'r'
            else:
                result += 'b'
        elif colours[i] == 'y':
            if colours[i+1] == 'b':
                result += 'r'
            elif colours[i+1] == 'r':
                result += 'b'
            else:
                result += 'y'
        elif colours[i] == 'b':
            if colours[i+1] == 'r':
                result += 'y'
            elif colours[i+1] == 'y':
                result += 'r'
            else:
                result += 'b'
    return colour_trio(result)


# colour_trio = lambda x: mixes[x] if len(x) <= 2 else colour_trio(''.join(mixes[x[i:i+2]] for i in range(len(x)-1)))

# def colour_trio(colours):
#     return dct_colours[colours] if len(colours) <= 2 else colour_trio(''.join(dct_colours[colours[i:i+2]] for i in range(len(colours)-1)))

def give_change(amount, coins):
    # Initialize the list
    result = []
    # If the amount is not 0
    while amount != 0:
        # Set get the largest value of coin from coins
        max_value = max(coins)
        # if the max_value is greater than amount, then get rid of that element
        if max_value > amount:
            coins.remove(max_value)
        # Else go through the for loop that repeats quotient amount of times and however many coins were needed
        for i in range(amount // max_value):
            result.append(max_value)
        # The amount is the remainder after the max_number of coins were used
        amount %= max_value
    # Return the result
    return result


def taxi_zum_zum(moves):
    # The motion is mapped on a cartesian plane
    # Starting position is looking forward
    degree = 90
    x_axis = 0
    y_axis = 0
    for i in moves:
        # If Left then add 90 to degree
        # If right then subtract 90 from degree
        if i == 'L':
            degree += 90
        elif i == 'R':
            degree -= 90
        # If the movement is Front, then add or subtract to x or y axis based on the direction the pointer is looking
        if i == 'F':
            main_degree = degree % 360
            if main_degree == 0:
                x_axis += 1
            elif main_degree == 180:
                x_axis -= 1
            elif main_degree == 90:
                y_axis += 1
            elif main_degree == 270:
                y_axis -= 1
    # Return the tuple with x and y co-ordinates
    return x_axis, y_axis

def safe_squares_rooks(n, rooks):
    # Create a chess board of size n
    board = [1] * (n * n)
    for i in rooks:
        # Get the row and the column from the tuple in rooks
        row = i[0]
        column = i[1]
        for j in range(n):
            # Change the rows and the columns of the rooks to 0
            board[(row * n) + j] = 0
            board[(n * j) + column] = 0
    # Return the final sum which would involve only 1s
    return sum(board)

def count_dominators(ls):
    if ls == []:
        return 0
    max_i = ls[len(ls)-1]
    dominator = 1
    for i in range(len(ls)-1,-1,-1):
        if ls[i] > max_i:
            max_i = ls[i]
            dominator += 1
    return dominator

def tukeys_ninthers(items):
    while True:
        if len(items) == 1:
            return items[0]
        if len(items) == 3:
            items.sort()
            return items[1]
        finallist = [items.pop(0), items.pop(0), items.pop(0)]
        finallist.sort()
        items.append(finallist[1])

def extract_increasing(digits):
    i = 1
    # Start result with the first digit inside the list already
    result = [int(digits[0])]
    while i < len(digits):
        # If the next number is greater than the last number, add that to the result list
        if result[-1] < int(digits[i]):
            result.append(int(digits[i]))
        else:
            # Create a temporary string
            num = '0'
            # Store the position of the current index
            previous_i = i
            # As long as the length of the digits has not exceeded and num is less than the last element of the result
            # Change num by string slicing from previous index to current index + 1
            while int(num) <= result[-1] and i < len(digits):
                i += 1
                num = digits[previous_i:i + 1]
            # If the num is then greater than the last element of result, add that to the list
            if int(num) > result[-1]:
                result.append(int(num))
        # Update the i value
        i += 1
    # Return the final list with the all ascending numbers
    return result