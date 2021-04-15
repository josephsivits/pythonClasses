# polymorphism -Class methods
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


obj1 = computer()
obj2 = math()

for dept in (obj1, obj2):
    dept.programs()
    dept.courses()
    dept.students()
