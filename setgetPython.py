'''
sname and degree
set, get, print methods


'''

class Student():
    def __init__(self):
        self.name = ""
        self.degree = ""

    def setName(self, n):
        self.name = n
    def setDegree(self, d):
        self.degree = d

    def getName(self):
        return self.name
    def getDegree(self):
        return self.degree 


    def printStudent(self):
        print("Name:", self.getName(),"\nDegree:",self.getDegree())




s = Student()
name = input("What is your name: ")
degree = input("What is your degree: ")
s.setName(name)
s.setDegree(degree)

s.printStudent()

