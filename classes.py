class Student():
    def __init__(self, name, id, coolStatus):
        self.name = name
        self.id = id
        self.coolStatus = coolStatus

    def printNameAndID(self):
        print(self.name, self.id, self.coolStatus)


getNameAndID = Student(input(), input(), input())

getNameAndID.printNameAndID()
