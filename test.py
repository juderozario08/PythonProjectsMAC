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

# Write a function sumIndices(string), which considers each letter of the parameter string and checks what is the
# index of that letter in the alphabet, and adds that index to a running sum.  (The find() method will help).
# The function prints the sum of the indices.  If a letter is not found in the alphabet, then -1 is added to the sum.
# Thus sumIndices('ab') is 1 because 'a' has index 0 in the alphabet, and 'b' has index 1 and 0 + 1 is 1.
# Similarly sumIndices('cab') is 3.  However, sumIndices('cab.') is 2, since '.' is not in the alphabet and it contributes -1.
# Note, alphabet is 'abcdefghijklmnopqrstuvwxyz'.  You can assume that capital letters are not in the alphabet.
