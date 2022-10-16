# Within the function:
# Iterate over the list contents using some kind of loop. If the integer at that position is not equal to 4, set the value at that list index to now be equal to that integer
# multiplied by your input scalar.
# However, if your list item at any index is equal to 4, then don't multiply it by the scalar and keep it as it is!
# After you have looped through the whole list and multiplied the scalar throughout (accounting for special 4 behaviour), return the updated list.

# Outside of the function (in the if __name__ == "__main__" block):
# First create an empty list.
# Then, set some integer num_ints to user input, representing the amount of integers that should be added to the list.
# Prompt the user to enter an integer num_ints times, and for each integer they enter add it to the list.
# Then, prompt the user to enter some scalar value that will be multiplied into the list.
# Finally, print the call of the above function using the (now non-empty) list and the integer as inputs.

def operation(ls,scalar):
    # The set function automatically gets rid of all the duplicates inside a list.
    # If the length of the original list and the length of the list after the removal of duplicates are not the same
    # That means that there were duplicates and hence we can return -1.
    # Create an empty list
    updatedLs = []
    # Iterate through the users list and check if the number is 4
    # If it is not, then multiply the scalar to it
    # Else just add the number in the list
    for i in range(len(ls)):
        if ls[i] != 4:
            updatedLs.append(ls[i]*scalar)
        else:
            updatedLs.append(ls[i])
    # Return the updated list
    return updatedLs

if __name__ == "__main__":
    # A bool to remember if there is a duplicate
    duplicatesBool = False
    # Create an empty list
    ls = []
    # Get input from the user for how many numbers they want
    size = int(input("How many numbers? "))
    # Go through a for loop and add the user inputs for the numbers in the list
    # After every input, check if the number already exists in the list.
    # If it exists then update then make sure the value for duplicates is True.
    # If the bool value is true, then return -1 else return then get the scalar and the updated list
    for i in range(size):
        number = int(input("Number: ")) 
        if number in ls:
            duplicatesBool = True
            break
        else:
            ls.append(number)
    if not duplicatesBool:
        # Get the scalar input from the user
        scalar = int(input("Enter Scalar Value: "))
        # Print the final updated list using another function by passing in the user created list and the scalar
        print(operation(ls, scalar))
    else:
        print("-1")
