# Write a Python program that will take one input from the user made up of two strings separated by a comma and a space (see samples below).
# Then create a mixed string with alternative characters from each string. Any leftover chars will be appended at the end of the resulting string.
# [ Do not use lists for this task]


def alternatingString(string):
    return ''.join([string[0:string.find(", ")][i:i+1]+string[string.find(", ") + 2:len(string)][i:i+1]
                    for i in range(max(len(string[0:string.find(", ")]), len(string[string.find(", ") + 2:len(string)])))])


# print(alternatingString("ABCD, efgh") == "AeBfCgDh" and alternatingString("ABCDENDFGH, ijkl")
#       == "AiBjCkDlENDFGH" and alternatingString("ijkl, ABCDENDFGH") == "iAjBkClDENDFGH")

# def removeDuplicates(string):
#     result = ''  # Empty string for storing the chracters
#     # Loop through the string
#     for i in string:
#         # If the character in the final index does not match the current character,
#         # add it to the result
#         if result[len(result)-1::] != i:
#             result += i
#     # Return the result
#     return result


# print(removeDuplicates('Jupyter Notebook is better. Case sensitivity check AAaaaAaaAAAa.') == 'Jupyter Notebok is beter. Case sensitivity check AaAaAa.'
#       and removeDuplicates('AAABBBBCDDBBECE') == 'ABCDBECE')

def x(string): return ''.join(
    [string[i] for i in range(len(string)) if string[i:i+1] != string[i-1:i]])


# print(x('Jupyter Notebook is better. Case sensitivity check AAaaaAaaAAAa.') ==
#       'Jupyter Notebok is beter. Case sensitivity check AaAaAa.' and x('AAABBBBCDDBBECE') == 'ABCDBECE')

def fibn(number):
    # Assume the first 2 fibonnaci numbers
    firstFibN = 0
    secondFibN = 1
    # Variable for storing the result
    result = 0
    # Print the first 2 numbers
    print(firstFibN, secondFibN, end=' ')
    # Forever while loop
    while True:
        # Result is always equal to the previous 2 fibonnaci numbers
        result = firstFibN + secondFibN
        # First fibonnaci numbers changes to the 2nd fibonnaci number
        firstFibN = secondFibN
        # Second fibonnaci number changes to the new result
        secondFibN = result
        # If the result > the number provided, break the loop
        if result > number:
            break
        # Print the number
        print(result, end=' ')


# fibn(15)

def perfNumberAndPrimes(start, stop):
    primes = []
    perfectNumbers = []
    primeFound = True
    for i in range(start, stop+1):
        count = 0
        for j in range(i):
            if j >= 1:
                if i % j == 0:
                    count += j
                    if j != 1:
                        primeFound = False
            if j == i-1:
                if count == i:
                    perfectNumbers.append(count)
                if primeFound:
                    primes.append(i)
        primeFound = True
    print(primes)
    print(perfectNumbers)


perfNumberAndPrimes(int(input("Enter Start Range: ")),
                    int(input("Enter Stop Range: ")))
