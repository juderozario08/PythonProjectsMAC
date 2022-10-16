from studentclass import Student
from studentclass import Questions

# This list stores the questions for the test
question_prompt = [
    "What is the colour of an apple? \na) Yellow\nb) Red\nc) Magenta\n",
    "What is the name of an animal with really long necks?\na) Giraffe\nb) Raccoon\nc) Cat\n",
    "What is the first element in the periodic table?\na) Nitrogen\nb) Chlorine\nc) Hydrogen\n"
]
# Ask for name, age, gpa and major course
name = input("Input Name: ")
while True:
    try : # Continue asking until it reaches else and breaks through the loop (except works like an if statement)
        age = 0
        while age < 1 or age > 90:
            age = int(input("Input Age: "))
    except ValueError as error:
        print(error)
        continue
    else:
        break
while True:
    try:
        gpa = float(input("Input GPA: "))
    except  ValueError as error:
        print(error)
        continue
    else:
        break
major = input("Input Major Course: ")
# Store the student info in another variable
student = Student(name, age, gpa, major)
# Store the test questions with the correct answers
questions = [
    Questions(question_prompt[0], "b"),
    Questions(question_prompt[1], "a"),
    Questions(question_prompt[2], "c")
]
# Open file
# Run the test
def run_test(questions):
    score = 0  # Initialize the score
    for question in questions:
        answer = input(question.prompt) # Print the Question and ask the user for an answer
        if question.answer == answer.lower(): # Check if the answer matches
            score += 1
    print("Name: " + student.name)
    print("Age: " + str(student.age))
    print("GPA: " + str(student.gpa))
    print("Major: " + student.major)
    print("You got " + str(score) + " / " + str(len(questions)) + " correct.")  
    if student.on_honour_roll() == True: # Print if the student has an honour roll  
        print("Student is on honour roll.\n")
    else:
        print("Student is not on the honour roll.\n")
run_test(questions)