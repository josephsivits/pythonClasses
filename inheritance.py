# base class
class Person:
    def __init__(self,name):
        self.name = name
    # get the name
    def getName(self):
        return self.name
    def isStudent(self):
        return False

#inherited class
class Student(Person):
    def isStudent(self):
        return True

# driver code
p1 = Person("Selva")
print(p1.getName(),p1.isStudent())
p2 = Student("Joseph")
print(p2.getName(),p2.isStudent())