# polymorphism -including Functions and Objects
class computer:
    def programs(self):
        print("Undergraduate and Graduate Programs")

    def courses(self):
        print("Computer Science1")
        print("Software Engineering")

    def students(self):
        print("Undergraduate: 65")
        print("Graduate:17")


class math:
    def programs(self):
        print("Undergrate-Maths")

    def courses(self):
        print("Discrete Mathematics")

    def students(self):
        print("undergradute: 60")


def CUC(obj):
    obj.programs()
    obj.courses()
    obj.students()


obj1 = computer()
obj2 = math()

CUC(obj1)
CUC(obj2)
