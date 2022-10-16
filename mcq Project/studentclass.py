class Student:
    def __init__(self, name, age, gpa, major):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.major = major
    
    def on_honour_roll(self):
        if float(self.gpa) >= 3.5:
            return True
        else:
            return False

class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer