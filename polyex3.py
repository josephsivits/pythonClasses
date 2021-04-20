# polymorphism with Inheritance
class College():
    def details(self):
        print("Concordia University Chicago")

    def programs(self):
        print("Doctorate, Graduate, Undergradaute and Certification Programs")


class Computer(College):
    # Here, process of re-implementing a method in the child class is known as Method Overriding
    def programs(self):
        print("Undergraduate-Computer Science")
        print("Undergraduate-Computer Information Systems")
        print("Graduate- Computer Science")

    def students(self):
        print("Undergraduate: 65")
        print("Graduate:17")


class Math(College):
    def programs(self):
        print("Undergraduate-Mathematics")
        print("Undergraduate-Mathematics Education")

    def students(self):
        print("Undergraduate: 60")


obj = College()
obj1 = Computer()
obj2 = Math()

obj.details()
obj.programs()

obj1.details()
obj1.programs()
obj1.students()

obj2.details()
obj2.programs()
obj2.students()
