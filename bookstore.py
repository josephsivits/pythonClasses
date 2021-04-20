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
crsr.executescript("""
CREATE TABLE Author(authorId integer primary key,
fName varchar(20),
lName varchar(30));

CREATE TABLE Publisher(pubId integer primary key,
pubName varchar(30),
pubAddress varchar(50));

CREATE TABLE Titles(ISBN integer primary key,
title varchar(20),
copyright integer(4),
authorId integer);

insert into Author values(1,"Joseph","Sivits");
insert into Author values(2,"Christian","Solis");
insert into Author values(3,"Selvanayaki","KS");

insert into Publisher values(100,"Concordia Publishing House","1234 CUC Street, St. Louis, MO");
insert into Publisher values(200,"Chicago Publishing","4555 Lake Street, Chicago, IL");
insert into Publisher values(300,"Capital Publishing","69420 Pennslyvania Ave, Washington D.C.");

insert into Titles values(1838138,"Big Baller Bigger Dubs",2020,1);
insert into Titles values(1655223,"Joe in Paris",2008,1);
insert into Titles values(5554132,"Christian and the CUC boys",2021,2);
insert into Titles values(5444132,"YO: The story of the kid who wouldn't quit.",2013,2);
insert into Titles values(2131214,"Python Programming",2006,3);
""")

# 2.	Select all authors from authors table
crsr.execute("select * from Author")
ans = crsr.fetchall()
print(ans)

# 3.	Select all publihser from the publishers table
crsr.execute("select * from Publisher")
ans = crsr.fetchall()
print(ans)

# 4.	Select a specific author and list all books
print("Showing books by Joseph Sivits")
crsr.execute("select * from Titles where authorId = 1")
ans = crsr.fetchall()
print(ans)

# commit the connection
connection.commit()
# close the connection
connection.close()