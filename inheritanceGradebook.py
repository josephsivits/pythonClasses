# 03/16/2021
'''
Get number of courses registered for the spring
get the course code and marks
then calculate the total and average of the marks
then print the details

do this inside of a grades funciton

'''
'''
class Student:
    def __init__(self, name, degree, year):
        self.name = name
        self.degree = degree
        self.year = year
    
    def welcome(self):
        print("Name " + self.name)
        print("Degree " + self.degree)
        print("Year " + self.year)

    def grades(self):
        coursesNumber = int(input("Enter number of courses: "))
        courses = []
        grades = []
        totalMarks = 0
        for i in range(0, coursesNumber):
            course = input("Enter course code: ")
            mark = int(input("Enter course mark: "))
            courses.append(course)
            grades.append(mark)
            totalMarks += mark
        averageMarks = (totalMarks / coursesNumber)
        print("Spring 2021\n")
        for i in range(0,coursesNumber):
            print(courses[i], ": ", grades[i])
        print("Total points: ", totalMarks)
        print("Average marks: ", averageMarks)

name = input("Enter your name: ")
degree = input("Enter degree: ")
year = input("Enter year of study: ")

st = Student(name,degree,year)
st.welcome()
st.grades()
'''
            
    
class Student:
    def __init__(self, name, degree, year):
        self.name = name
        self.degree = degree
        self.year = year

    def welcome(self):
        print("Name " + self.name)
        print("Degree " + self.degree)
        print("Year " + self.year)

class Grades(Student):
    def setGrades(self):
        coursesNumber = int(input("Enter number of courses: "))
        courses = []
        grades = []
        totalMarks = 0

        for i in range(0, coursesNumber):
            course = input("Enter course code: ")
            mark = int(input("Enter course mark: "))
            courses.append(course)
            grades.append(mark)
            totalMarks += mark

    def printGrades(self):
        print("Spring 2021\n")
        for i in range(0,self.coursesNumber):
            print(courses[i], ": ", grades[i])

        print("Total points: ", totalMarks)
        print("Average marks: ", averageMarks)


    