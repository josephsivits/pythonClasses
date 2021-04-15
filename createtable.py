# importing module
import sqlite3

# connecting to the database
connection = sqlite3.connect("mytable.db")

# Cursor
crsr = connection.cursor()

# if first time running need node below
#   SQL command to delete the table
sql_cmd = """Drop table s_emp;"""
#   execute the statement
crsr.execute(sql_cmd)

# SQL command to create a table in the database
sql_cmd = """create table s_emp(staff_number integer primary key,
fname varchar(20),
lname varchar(30),
gender char(1),
joining DATE);"""
# execute the statement
crsr.execute(sql_cmd)

# SQL Command to insert the dataset1 in the table
sql_cmd = """insert into s_emp values(1,"Selvanayaki","KS","F","01-08-2018");"""
# execute the statement
crsr.execute(sql_cmd)
# SQL Command to insert the dataset1 in the table
sql_cmd = """insert into s_emp values(2,"Samira","Teja","F","01-08-2020");"""
# execute the statement
crsr.execute(sql_cmd)

# Execute the command to fetch the data from the table employee
crsr.execute("select * from s_emp")
# Fetch the data in the ans variable
ans = crsr.fetchall()
# Print the data
print(ans)
# connection.commit()
connection.commit()

# close the connection
connection.close()
