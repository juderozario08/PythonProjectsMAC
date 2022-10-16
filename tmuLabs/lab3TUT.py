####### LAB 3 TUT ######\

def backwardsSort(ls):
    updatedLs = [] # Empty List
    while len(ls) != 0: # Loop until the length of the original list is 0
        updatedLs.append(max(ls)) # Append the max value of the original list to the updated list
        ls.remove(max(ls)) # Remove the first instance of the max value
    return updatedLs # return the updated list

if __name__ == '__main__':
    ls = [] # Empty List
    size = int(input("Size of List: ")) # Ask user for the number of strings they want to input
    for i in range(size): # Loop size number of times, size being the number of items in the list
        ls.append(input(f"Enter String {i+1}: ")) # Ask user for the inputs for the strings
    print(backwardsSort(ls)) # Print the returned updated list in the backwardsSort function.