import sqlite3

# connecting to the database
connection = sqlite3.connect("college.db")
crsr = connection.cursor()

# next 6 lines only necessary if running after first time
sql_cmd = """DROP TABLE Students;"""
crsr.execute(sql_cmd)

crsr.executescript("""
CREATE TABLE Students(studentID int primary key,
name varchar(30),
major varchar(30),
graduated bool,
gpa float);


INSERT INTO Students values(5028,"Joseph Sivits","Computer Science",0,3.81);
INSERT INTO Students values(9391,"Dragana Antic","Computer Science",1,3.92);
INSERT INTO Students values(1234,"Jose Cabrera","Computer Science",0,2.88);
INSERT INTO Students values(4421,"Eden Schult","Elementary Education",1,4.10);
INSERT INTO Students values(8323,"Roberto Jordan","Business Intelligence",0,3.22);
INSERT INTO Students values(4943,"Davis Bueltmann","Game Art",1,3.44);
INSERT INTO Students values(5566,"Ashley Kennedy","Mathematics",0,3.89);
""")


def sortByGPA():
    print("\n Sorted Students by GPA")
    crsr.execute("SELECT name, gpa FROM Students ORDER BY gpa DESC")
    p = crsr.fetchall()
    print(p,'\n')

def sortByMajor():
    crsr.execute("SELECT DISTINCT major FROM Students")
    print(crsr.fetchall())
    userInput = input("What major would you like to select: ")
   #script = "SELECT name, major FROM Students WHERE major ='",userInput,"';";
    crsr.execute("SELECT name, major FROM Students WHERE major = (?)",[userInput])
    p = crsr.fetchall()
    print(p,'\n')

def removeGrads():
    crsr.execute("SELECT name,major,gpa FROM Students WHERE graduated=false")
    p = crsr.fetchall()
    print(p,'\n')


def menu():
    choice = 0
    while choice != 6:
        print("1. Execute query sorting the students by gpa.")
        print("2. Print query sorting the students by gpa.")
        print("3. Execute query selecting studetns by major.")
        print("4. Print query selecting students by major.")
        print("5. Execute query removing graduated students.")
        print("6. Quit.")
        choice = int(input("?  "))
        if choice == 1 or choice == 2:
            sortByGPA()
        elif choice == 3 or choice == 4:
            sortByMajor()
        elif choice == 5:
            removeGrads()
        elif choice == 6:
            quit()
        else:
            print("ERROR! Invalid Input!")


menu()


connection.commit()
connection.close()