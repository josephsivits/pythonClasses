#program to show basisc of polymorphism 

class Account:
    def __init__(self):
        self.userName = ""
        self.password = ""
        self.id = 0


    def loginInfo(self):
        self.userName = input("Enter Username: ")
        self.password = input("Enter password: ")
        self.id = int(input("Enter id: "))

class ContactInfo(Account):
    def __init__(self):
        self.email = ""
        self.phone = 0
        a = Account()

    def loginInfo(self):
        self.userName = input("Enter your email: ")
        self.phone = int(input("Enter 10 digit phone number: "))
    
def acc(obj):
    obj.loginInfo()

ob1 = Account()
ob2 = ContactInfo()

acc(ob1)
acc(ob2)