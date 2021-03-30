'''
Employee Pay Stub
	Employee: ID, Name, Department, Designmation, DOB, Address
	Pay Details: Hourly/Monthly/Annually, Pay Rate/Pay, Allowances

Add the allowance of birthday with your paystub
	If your birthday is your current month, then add $100 to pay stub

Employee Base class
Allowance is derived class

2 functions for getting infor from the users


pay is 15 hours
input of montly pay
annual pay for the year

allowance class
inherits employee class
get input of the current month
adding the allowance to 100
print the salary details

2 funcitons, employee details and pay details

create a display class that inherits from an employee class

'''

class Employee:
    # maybe don't do init...
    def __init__(self):
        self.empSalary = 0

    def setBirthMonth(self):
        birthMonth = int(input("What is your birth month(1-12): "))
        if(birthMonth > 12 or birthMonth < 1):
            print("!ERROR! Invalid Input Not in Range\n")
            self.setBirthMonth()
        else:
            self.dobMonth=birthMonth

    def setBirthDate(self):
        birthDay = int(input("What is your birth day(1-31): "))
        monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
        if(birthDay > 31 or birthDay < 1):
            print("!ERROR! Invalid Input Not in Range\n")
            self.setBirthDate()
        elif(birthDay > monthDays[self.dobMonth - 1]):
            print("!ERROR! Day out of range for month\n")
            self.setBirthDate()
        else:
            self.dobDay=birthDay

        # 2 functions for getting inputs, employee details and pay details
    def employeeDetails(self):
        self.id=int(input("What is your employee ID: "))
        self.name=input("What is your name: ")
        self.department=input("What is your department: ")
        self.designation=input("What is your title: ")
        self.setBirthMonth()
        self.setBirthDate()
        
    def payDetails(self):
        self.payType = [0,0,0]
        payIndex = int(input("What type of pay are you\n0 = Hourly\n1 = Monthly\n2 = Annually\n"))
        if payIndex < 0 or payIndex > 2:
            print("!ERROR! Invalid Input Not in Range\n")
            self.payDetails()
        if payIndex == 0:
            hourPay = int(input("How many hours do you work in a month: "))
            self.payType[payIndex] = 15*hourPay
        elif payIndex == 1:
            monthPay = int(input("What is your monthly pay: "))
            self.payType[payIndex] = monthPay
        elif payIndex == 2:
            yearPay = int(input("What is your yearly salary: "))
            self.payType[payIndex] = (int(yearPay/12));

class Allowance(Employee):
    def __init__(self):
        self.salary = 0
        self.employeeDetails()
        self.payDetails()
        self.getCurrentMonth()
        self.printSalary()

    def getCurrentMonth(self):
        currMonth = int(input("What is the current month(0-12): "))
        if currMonth == self.dobMonth:
            print("Happy birthday! (month)")
            self.salary += 100

    def printSalary(self):
        for i in range(0,3):
            if self.payType[i] > 0:
                self.salary += self.payType[i]
                self.empSalary = self.salary
                print("Monthly Salary: ", self.salary)

# testing multiple inheritance I think
class Display(Employee):
    emp=Allowance()
    def printEmpSalary(self):
        print("Monthly Salary:", self.empSalary)

employee = Display()




    
