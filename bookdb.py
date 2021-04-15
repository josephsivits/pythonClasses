'''
REQUIREMENTS
consider a book database, which includes authors, publisher, titles tables
	Author		consists of authorId, firstName, lastName
	Publisher	consists of publisherId, publisherName, address
	Titles		Consists of ISBN, title, copyright

Perform the following tasks:
1.	Create the above db with all 3 tables
2.	Select all authors from authors table
3.	Select all publihser from the publishers table
4.	Select a specific author and list all books
'''
import sqlite3

# connecting to the database
connection = sqlite3.connect("library.db")
crsr = connection.cursor()

# next 6 lines only necessary if running after first time

sql_cmd = """DROP TABLE Author;"""
crsr.execute(sql_cmd)
sql_cmd = """DROP TABLE Publisher;"""
crsr.execute(sql_cmd)

sql_cmd = """DROP TABLE Titles;"""
crsr.execute(sql_cmd)


# 1.	Create the above db with all 3 tables
# SQL commands for initializing table(s)
sql_cmd = """CREATE TABLE Author(authorId integer primary key,
fName varchar(20),
lName varchar(30));"""
crsr.execute(sql_cmd);

sql_cmd = """CREATE TABLE Publisher(pubId integer primary key,
pubName varchar(30),
pubAddress varchar(50));"""
crsr.execute(sql_cmd)

sql_cmd = """CREATE TABLE Titles(ISBN integer primary key,
title varchar(20),
copyright integer(4),
authorId integer);"""
crsr.execute(sql_cmd)

#inserting into author database
sql_cmd = """insert into Author values(1,"Joseph","Sivits");"""
crsr.execute(sql_cmd)
sql_cmd = """insert into Author values(2,"Christian","Solis");"""
crsr.execute(sql_cmd)
sql_cmd = """insert into Author values(3,"Selvanayaki","KS");"""
crsr.execute(sql_cmd)

# 2.	Select all authors from authors table
crsr.execute("select * from Author")
ans = crsr.fetchall()
print(ans)

#inserting into publishing
sql_cmd = """insert into Publisher values(100,"Concordia Publishing House","1234 CUC Street, St. Louis, MO");"""
crsr.execute(sql_cmd)
sql_cmd = """insert into Publisher values(200,"Chicago Publishing","4555 Lake Street, Chicago, IL");"""
crsr.execute(sql_cmd)
sql_cmd = """insert into Publisher values(300,"Capital Publishing","69420 Pennslyvania Ave, Washington D.C.");"""
crsr.execute(sql_cmd)

# 3.	Select all publihser from the publishers table
crsr.execute("select * from Publisher")
ans = crsr.fetchall()
print(ans)

sql_cmd = """insert into Titles values(1838138,"Big Baller Bigger Dubs",2020,1);"""
crsr.execute(sql_cmd)
sql_cmd = """insert into Titles values(1655223,"Joe in Paris",2008,1);"""
crsr.execute(sql_cmd)
sql_cmd = """insert into Titles values(5554132,"Christian and the CUC boys",2021,2);"""
crsr.execute(sql_cmd)
sql_cmd = """insert into Titles values(5444132,"YO: The story of the kid who wouldn't quit.",2013,2);"""
crsr.execute(sql_cmd)
sql_cmd = """insert into Titles values(2131214,"Python Programming",2006,3);"""
crsr.execute(sql_cmd)

# 4.	Select a specific author and list all books
print("Showing books by Joseph Sivits")
crsr.execute("select * from Titles where authorId = 1")
ans = crsr.fetchall()
print(ans)

# commit the connection
connection.commit()
# close the connection
connection.close()