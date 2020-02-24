#install MySQL

import MySQLdb  #this is not a part of standard Python library set
                                                                            # Open database connection
"""
UserName : root
Password  : root
DB Name: test
"""
db = MySQLdb.connect("localhost","root","root","test" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         PASS CHAR(30),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

                                                                    #insert values into DB
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME,PASS, AGE, SEX, INCOME) \
       VALUES ('%s', '%s','%s', '%d', '%c', '%d' )" % \
       ('Ashish1', 'Surve1','Password1', 20, 'M',90000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

                                                                    #insert values into DB
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME,PASS, AGE, SEX, INCOME) \
       VALUES ('%s','%s', '%s', '%d', '%c', '%d' )" % \
       ('Ashish', 'Surve','Password2', 23, 'M',90000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME,PASS, AGE, SEX, INCOME) \
       VALUES ('%s','%s', '%s', '%d', '%c', '%d' )" % \
       ('Sunny', 'Khandare','Password2', 23, 'M',90000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME,PASS, AGE, SEX, INCOME) \
       VALUES ('%s','%s', '%s', '%d', '%c', '%d' )" % \
       ('Nikhil', 'Badgujar','Password2', 23, 'M',90000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME,PASS, AGE, SEX, INCOME) \
       VALUES ('%s','%s', '%s', '%d', '%c', '%d' )" % \
       ('Ayush', 'Agrawal','Password2', 23, 'M',90000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()



# disconnect from server
db.close()
