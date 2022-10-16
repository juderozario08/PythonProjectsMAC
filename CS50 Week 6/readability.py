passage = str(input("Input Message: "))
# Determine the number of words, letters and sentences by iterating through the string
word = 1
letters = 0
sentences = 0
for c in passage:
    if c == " ":  # If space is found add 1
        word += 1
    elif c.isalpha() or c.isnumeric():  # If the character is a digit or a number add 1
        letters += 1
    elif c == "!" or c == "?" or c == ".":
        sentences += 1
# Perform the algorith
index = float(0.0588 * (100 * (letters / word)) - 0.296 * (100 * (sentences / word)) - 15.8)
grade = round(index)  # Round the index to get an integer grade
if grade > 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")
