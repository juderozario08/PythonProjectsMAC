# Prompt user for a height
height = int(input("Input Number: "))

# Print the HASH's 
for i in range(height):
    for j in range(height):
        if (i+j) >= height-1:
            print("#", end='')
        else:
            print(" ", end='')
    
    print("  ", end='')
    
    for k in range(height):
        if k <= i:
            print("#", end='')
    print("")
