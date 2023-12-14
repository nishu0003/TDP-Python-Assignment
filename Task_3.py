"""
Task 3: MySQL Database Operations with Python ( Compulsory )
Problem Statement:
Your task is to write a Python program that accomplishes the following:
First create a database , table and add these column ‘student_id’, ‘first_name’, ‘last_name’,
‘age’, ‘grade’.
Connects to your MySQL database with python.
Inserts a new student record into the "students" table with the following details:
First Name: "Alice"
Last Name: "Smith"
Age: 18
Grade: 95.5
Updates the grade of the student with the first name "Alice" to 97.0.
Deletes the student with the last name "Smith."
Fetches and displays all student records from the "students" table.
"""

import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password='Nishu@3112000',
    database='db1') #first i made the database which i comment below after that i am using there

cur=mydb.cursor()
#cur.execute("CREATE DATABASE db1")

"""s="CREATE TABLE Student_details(student_id INT(4) PRIMARY KEY,first_name VARCHAR(20),last_name VARCHAR(20),age INT(2) NOT NULL,grade FLOAT(5,2))"
cur.execute(s)"""        #here i made student details table and define them

n=int(input("How many Students data you want to add : "))             #here we will input how many students data we want to add in our database.
for x in range(n):                 #inside that loop we addup the n number of students data. 
    id=input("ENter the id of {} student : ".format(str(x+1)))
    fname=input("ENter the first name of student : ")
    lname=input("ENter the last name of student : ")
    age=input('Enter the age of student : ')
    grade=input("ENter the grades of student :")
    m="INSERT INTO Student_details (student_id,first_name,last_name,age,grade) Values(%s,%s,%s,%s,%s)"
    b1=(id,fname,lname,age,grade)
    cur.execute(m,b1)
    mydb.commit()
u="UPDATE Student_details set grade='97.0' WHERE first_name='Alice'"           #here we are updating the grades of student whose first name is 'Alice'. 
cur.execute(u)
mydb.commit()
d="DELETE FROM Student_details WHERE last_name='Smith'"              #here we delete the student details whose last name is 'Smith'.
cur.execute(d)
mydb.commit()
