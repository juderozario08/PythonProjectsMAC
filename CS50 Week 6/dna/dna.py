from sys import exit, argv
import csv

def main():
    # If the proper command line argument is not present, exit program
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # Get the path of the database file from the input and open the file
    database_path = argv[1]
    database = open(database_path)

    # Read the databases .csv file using DictReader and then store the DNA strands is a list separately
    database_reader = csv.DictReader(database)
    strands_group = database_reader.fieldnames[1:]

    # Open the DNA file using the input and then copy the file
    dna_path = argv[2]
    dna_file = open(dna_path)
    dna = dna_file.read()
    dna_file.close() # Close file

    # Introduce a dictionary to store all the values of the Strands with proper indexing
    dnadict = {}

    # Go through the group of strands and check for how many times they repeat in the DNA
    for strands in strands_group:
        # Call this function to find the number of reptitions
        numofstrands = repetitions(dna, strands)
        # Set the value of the particular strand to the number of Reps
        dnadict[strands] = numofstrands

    # Read through all the rows of the Database file and check if all the values match
    for row in database_reader:
        # Pass the list of strands, dna dictionary, the row I am looking at
        if match(strands_group, dnadict, row):
            print(row['name']) # Print the name of the person in the row whose values matched
            database.close() # Close file and exit program
            exit(0)

    print("No Match\n")
    exit(1)

# Match the list of values on the dnadict with the values in the Database file
def match(strands_group, dnadict, row):
    # Loop through each strand in the list
    for strands in strands_group:
        # Search for the particular strand in the DNA Dictionary
        # Match the values of that strand with the values in the row of the same strand in the database file
        if dnadict[strands] != int(row[strands]):
            return False # Return false if the values do not match
    return True

# Algorithm for how many times a strand repeats
def repetitions(dna, strands):
    i = 0
    # strands = AGGAT * 1 = AGGAT
    # strands = AGGAT * 2 = AGGATAGGAT
    while strands*(i + 1) in dna:
        i += 1
    return i

main()